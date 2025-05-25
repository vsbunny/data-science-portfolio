# Housing Price Prediction API (FastAPI)

This folder contains a lightweight RESTful API built with FastAPI. Its primary purpose is to serve predictions from the pre-trained Random Forest Regressor model for California median house values. It allows users to input housing features via a web service and receive a predicted value.

## Contents

* `main.py`: The core FastAPI application code.
* `random_forest_model.pkl`: The pre-trained Random Forest model, managed by Git LFS.
* `feature_names.pkl`: A serialized list of the feature names in the order the model expects (for reference).
* `requirements.txt`: Python dependencies specifically required for this API.

## How to Run the API

1.  **Navigate to this directory** in your terminal:
    ```bash
    cd California_housing_dataset/house_price_API/
    ```
2.  **Install API-specific dependencies:**
    (It's highly recommended to do this within a dedicated Python virtual environment.)
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the FastAPI application:**
    ```bash
    uvicorn main:app --reload
    ```
    The `--reload` flag is useful for development, automatically restarting the server on code changes.

## How to Test the API

Once the API is running (you will see messages in your terminal indicating it's serving, typically on `http://127.0.0.1:8000`), open your web browser and go to:

* **Interactive Documentation (Swagger UI):** `http://127.0.0.1:8000/docs`
    * Here, you can directly test the `/predict_house_value/` endpoint by clicking "Try it out", entering example feature values, and clicking "Execute".
* **Root Endpoint:** `http://127.0.0.1:8000` (for a simple welcome message)

## Author

[Vanya Fernandez Galabo]