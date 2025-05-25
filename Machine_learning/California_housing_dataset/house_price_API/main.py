# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import numpy as np
import joblib # To load your saved model
import os # For checking if the model file exists

# --- 1. Load the Trained Random Forest Model ---
# Ensure the 'random_forest_model.pkl' is in the same directory as this script,
# or provide the full path to it.
MODEL_PATH = 'random_forest_model.pkl'

try:
    # Attempt to load the model. joblib is recommended for scikit-learn models.
    model = joblib.load(MODEL_PATH)
    print(f"Random Forest model loaded successfully from {MODEL_PATH}")
except FileNotFoundError:
    print(f"Error: Model file '{MODEL_PATH}' not found. Please ensure it's in the correct directory.")
    model = None # Set model to None if loading fails, to prevent further errors
except Exception as e:
    print(f"An error occurred while loading the model: {e}")
    model = None


# --- 2. Initialize FastAPI App ---
# Create an instance of the FastAPI application.
app = FastAPI(
    title="California Housing Price Predictor API",
    description="Predicts median house values based on features using a pre-trained Random Forest Regressor.",
    version="1.0.0"
)

# --- 3. Define Input Data Model (Pydantic) ---
# This class defines the structure and types of the data that your API will expect
# in the request body when someone wants to make a prediction.
# The fields here correspond to the ORIGINAL 4 features the model *internally* uses for feature engineering.
class HouseFeatures(BaseModel):
    MedInc: float = Field(..., description="Median income for households in the block group (in $10,000s).")
    HouseAge: float = Field(..., description="Median house age in the block group.")
    AveRooms: float = Field(..., description="Average number of rooms per household.")
    Population: float = Field(..., description="Block group population.")

    # Add example values for the API documentation (Swagger UI)
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "MedInc": 3.8723,
                    "HouseAge": 32.0,
                    "AveRooms": 5.0,
                    "Population": 1200.0
                }
            ]
        }
    }


# --- 4. Define Prediction Endpoint ---
# This is the main endpoint where users will send data to get a prediction.
@app.post("/predict_house_value/", response_model=dict, summary="Predict median house value")
async def predict_house_value(features: HouseFeatures):
    """
    Accepts a set of house features and returns the predicted median house value.
    The API performs internal feature engineering (polynomial, log, interaction terms)
    before making the prediction using the loaded Random Forest model.
    """
    if model is None:
        raise HTTPException(status_code=500, detail="Prediction model is not loaded.")

    # Extract original features from the incoming request data.
    medinc = features.MedInc
    houseage = features.HouseAge
    averooms = features.AveRooms
    population = features.Population

    # --- Re-perform the exact same Feature Engineering steps as during model training ---
    # This is ABSOLUTELY CRUCIAL. The model expects input in the exact same format
    # it was trained on (same features, same order, same transformations).
    medinc_sq = medinc**2
    log_population = np.log1p(population) # Use np.log1p for consistency with training
    medinc_x_averooms = medinc * averooms

    # Create a NumPy array for the model prediction.
    # The order of features in this array MUST match the order used during model training.
    # The order was: ['MedInc', 'HouseAge', 'AveRooms', 'Population', 'MedInc_Sq', 'Log_Population', 'MedInc_x_AveRooms']
    input_data_array = np.array([
        medinc,
        houseage,
        averooms,
        population,
        medinc_sq,            # Engineered feature
        log_population,       # Engineered feature
        medinc_x_averooms     # Engineered feature
    ]).reshape(1, -1) # .reshape(1, -1) reshapes the array to be 1 sample with N features.

    # Make the prediction using the loaded Random Forest model.
    prediction = model.predict(input_data_array)[0] # [0] extracts the scalar prediction value.

    # Return the prediction as a JSON response.
    return {"predicted_median_house_value": float(prediction)}


# --- 5. Root Endpoint (Optional) ---
# A simple endpoint to confirm the API is running.
@app.get("/", summary="Root endpoint")
async def root():
    """
    Returns a welcome message for the API.
    """
    return {"message": "Welcome to the California Housing Price Predictor API! Visit /docs for interactive API documentation."}
