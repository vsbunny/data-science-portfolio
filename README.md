# Vanya Fernandez Galabo - Data Science Portfolio

[![Python Version](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

## Description

A comprehensive collection of data science projects showcasing hands-on skills in machine learning, statistical modeling, data acquisition, and deployment. This portfolio highlights an iterative problem-solving approach, technical proficiency, and the ability to work with diverse datasets and tools.

## Highlights

* **End-to-end Machine Learning Workflow:** From data preprocessing and model development to performance evaluation and API deployment.
* **Advanced Statistical Modeling:** Application of Bayesian inference and nested sampling for complex scientific parameter estimation.
* **Data Acquisition & Web Scraping:** Expertise in extracting structured data from various web sources, including dynamic content, using frameworks like Scrapy and libraries like Beautiful Soup.
* **Model Optimization & Comparison:** Demonstrated ability to optimize model performance through vectorization and feature engineering, alongside critical comparison of different model types (Linear Regression vs. Random Forest).
* **API Development for Model Serving:** Practical experience in deploying machine learning models as accessible web services using FastAPI.
* **Robust Code & Documentation:** Commitment to writing clean, well-commented code and creating comprehensive project documentation.

## Project List

Here's an overview of the projects included in this portfolio:

* ### [California Housing Price Prediction (Linear Regression & Random Forest)](./Machine_learning/California_housing_dataset/README.md)
    An in-depth exploration of housing price prediction, showcasing iterative model development, extensive feature engineering, vectorized computations, and a comparison between Linear Regression and Random Forest models. Includes a deployed API for prediction.

* ### [Cosmological Parameter Estimation (Bayesian Inference with cpnest)](./Observational_cosmology/README.md)
    A scientific computing project focused on estimating fundamental cosmological parameters from observational data using advanced Bayesian inference and nested sampling techniques with the `cpnest` library.

* ### Web Scrapers: Data Acquisition & Analysis
    A collection of web scraping projects demonstrating versatile data acquisition and processing techniques.

    * #### [QS World University Rankings Scraper & Data Wrangling](./Scraping_projects/QS_world_rankings/README.md)
        This project focuses on extracting detailed university ranking data from the QS World University Rankings website using Scrapy with Selenium for dynamic content, followed by data wrangling with Pandas.

    * #### [Times Higher Education (THE) World University Rankings Scraper & Data Wrangling](./Scraping_projects/THE_world_rankings/README.md)
        This project utilises Selenium and Beautiful Soup for efficient extraction of university rankings from the Times Higher Education website, combined with Pandas for subsequent data processing and standardization.

## Setup & Running the Portfolio

To explore all projects in this portfolio:

1.  **Clone the entire repository:**
    ```bash
    git clone [https://github.com/vsbunny/data-science-portfolio.git](https://github.com/vsbunny/data-science-portfolio.git)
    cd data-science-portfolio
    ```

2.  **Install Git Large File Storage (Git LFS):**
    This repository uses Git LFS to manage large model files. Follow instructions on [https://git-lfs.github.com/](https://git-lfs.github.com/) to install it, then run `git lfs install` in your terminal. If you cloned before installing LFS, run `git lfs pull` from the repository root.


3.  **Navigate to individual project folders:**
    Each project (`California_housing_dataset/`, `Observational_cosmology/`, `Scraping_projects/`) has its own `README.md` with specific installation steps (e.g., WebDriver for web scrapers, specific Python versions for cosmology) and usage instructions for running notebooks or scripts. Please refer to those for detailed guidance.

## Author

[Vanya Fernandez Galabo] 

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.