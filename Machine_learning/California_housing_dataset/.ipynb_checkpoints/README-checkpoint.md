# California Housing Price Prediction: An Iterative Machine Learning Approach

[![Python Version](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](../../LICENSE) ## Description

This project explores various linear regression models and a Random Forest Regressor to predict median house values in California, based on the California Housing dataset. It highlights an iterative approach to model improvement, starting from a simple linear model and addressing challenges of non-linearity and heteroscedasticity through advanced techniques.

## Project Structure
.
├── README.md                           <- This file
├── Vectorization_efficiency.ipynb      <- Demonstrates the efficiency of vectorized operations
├── PartOne_LRModel_OneFeature.ipynb         <- Initial Linear Regression with one feature
├── PartTwo_LRModel_MultipleFeatures.ipynb   <- Multiple features, vectorization, and initial feature engineering (Model V1 & V2)
├── PartThree_RandomForest.ipynb        <- Random Forest Regressor implementation and comparison
├── requirements.txt                    <- Packages necessary for this project
└── house_price_API/                         <- Subfolder containing the FastAPI prediction API
 ├── main.py
 ├── random_forest_model.pkl
 ├── feature_names.pkl
 └── requirements.txt
 └── RandomForest.ipynb
 
 
## Features / Highlights

* **Custom Vectorized Linear Regression:** Implements core machine learning concepts (cost function, gradient, gradient descent) using highly efficient NumPy vectorized operations for scalable computation.
* **Iterative Model Improvement:** Demonstrates a step-by-step process of model enhancement, from a single-feature baseline to a robust, multi-feature model, quantifying improvements at each stage.
* **Advanced Feature Engineering:** Showcases techniques to improve linear model performance, including:

    * Polynomial features (e.g., `MedInc^2`) to approximate non-linearity.
    * Logarithmic transformations (e.g., `log(Population)`) for skewed distributions and diminishing returns.
    * Interaction terms (e.g., `MedInc * AveRooms`) to capture complex feature dependencies.
    
* **Model Comparison & Selection:** Benchmarks the performance and limitations of Linear Regression (even with engineered features) against the more flexible Random Forest Regressor for non-linear datasets.
* **Handling Model Limitations:** Specifically addresses and visualizes challenges like heteroscedasticity and complex non-linear patterns, explaining how different models handle them.
* **Comprehensive Visualization:** Utilises Matplotlib for clear data exploration, convergence plots, and comparative prediction visualizations, using a distinct and professional color palette.
* **Model Deployment Fundamentals:** Includes a dedicated subfolder (`house_price_API/`) for API development to serve the trained Random Forest model.

## Installation and Setup

To get this project running on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/vsbunny/data-science-portfolio.git](https://github.com/vsbunny/data-science-portfolio.git)
    cd data-science-portfolio/California_housing_dataset
    ```

2.  **Install Git Large File Storage (Git LFS):**
    This repository uses Git LFS to manage large files (specifically, the trained Random Forest model in `housing_API/random_forest_model.pkl`). You need to install it to properly download and manage this file.
    * **macOS (Direct Download of Binaries):**
        * Go to [https://git-lfs.github.com/releases/](https://git-lfs.github.com/releases/).
        * Find the latest release (e.g., `v3.6.1`) and expand "Assets".
        * Download `git-lfs-X.Y.Z-darwin-amd64.zip` (for Intel Macs) or `git-lfs-X.Y.Z-darwin-arm64.zip` (for Apple Silicon Macs).
        * Open Terminal, `cd ~/Downloads`, `unzip your_downloaded_git_lfs.zip`.
        * `cd` into the extracted folder (e.g., `cd git-lfs-3.6.1`).
        * `sudo mv git-lfs /usr/local/bin/` (enter your Mac password if prompted).
    * **Initialize Git LFS:**
        ```bash
        git lfs install
        ```
    * **Pull LFS files:** If you cloned the repository *before* installing Git LFS, or if you had issues, navigate to the `California_housing_dataset` folder and run:
        ```bash
        git lfs pull
        ```

3.  **Create and activate a virtual environment (highly recommended):**
    ```bash
    python -m venv venv_housing_ml
    source venv_housing_ml/bin/activate # On Windows: .\venv_housing_ml\Scripts\activate
    ```

4.  **Install Python dependencies:**
    ```bash
    pip install -r ../requirements.txt
    ```
    (Note the `../` because `requirements.txt` is assumed to be in the root of `data-science-portfolio/`.)

## Usage

* **To explore the analysis and model development:**
    ```bash
    jupyter lab
    # Then open and run the .ipynb files sequentially within the browser:
    # Vectorization_efficiency.ipynb
    # PartOne_LRModel_OneFeature.ipynb
    # PartTwo_LRModel_MultipleFeatures.ipynb
    # PartThree_RandomForest.ipynb
    ```
* **To run the prediction API:**
    Refer to the dedicated `[house_price_API/README.md](house_price_API/README.md)` for detailed instructions on setting up and running the model deployment.

## Results and Insights

This project demonstrates that:

* Vectorization is crucial for building computationally efficient machine learning models in Python.
* Linear Regression, even with advanced feature engineering, has inherent limitations (e.g., struggling with heteroscedasticity and complex non-linear patterns) that constrain its predictive power for certain datasets.
* Models like Random Forest Regressor are significantly more adept at capturing complex data relationships without extensive manual feature engineering, leading to superior performance (e.g., visually evident improvement in 'MedInc' predictions).
* The overall project workflow showcases an iterative approach to problem-solving, model selection, and performance optimization in machine learning.

## Future Work

* Explore hyperparameter tuning for the Random Forest model to further optimize its performance.
* Investigate other advanced ensemble methods (e.g., Gradient Boosting Machines).
* Consider more advanced feature engineering techniques or polynomial degrees for the linear model.

## Author

[Vanya Fernandez Galabo]