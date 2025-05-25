# Cosmological Parameter Estimation: Bayesian Inference with cpnest

[![Python Version](https://img.shields.io/badge/Python-3.7-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](../../LICENSE) ## Description

This project applies advanced Bayesian inference techniques to estimate key cosmological parameters from observational data (likely Supernovae data from`supernovae_data.dat`). It utilizes the `cpnest` library, a powerful and efficient Python package for nested sampling, to perform robust parameter estimation and quantify uncertainties across different cosmological models (Flat, Closed, and Open Universes).

## Project Structure
```
.
├── README.md               <- This file
├── ObsCosNest_flat.py           <- Python script for fitting a Flat Universe model (Ω_m + Ω_Λ = 1)
├── ObsCosNest_closed.py         <- Python script for fitting a Closed Universe model (Ω_m + Ω_Λ > 1)
├── ObsCosNest_open.py           <- Python script for fitting an Open Universe model (Ω_m + Ω_Λ < 1)
├── Cornerplot_flat.py           <- Python script to generate corner plots from cpnest posterior samples
├── Cornerplot_closed.py         <- Python script to generate corner plots from cpnest posterior samples
├── Cornerplot_open.py           <- Python script to generate corner plots from cpnest posterior samples
├── supernovae_data.dat          <- Input observational data for cosmological analysis (e.g., Supernovae data)
├── Run_files_flat/         <- Output directory for results from Flat Model (cpnest output files)
├── Run_files_closed/       <- Output directory for results from Closed Model (cpnest output files)
├── Run_files_open/         <- Output directory for results from Open Model (cpnest output files)
├── Corner_plots/           <- Output directory for generated corner plots (PNG images)
└── requirements.txt        <- Python dependencies specific to this project
```


## Features / Highlights

* **Advanced Bayesian Inference:** Application of Bayes' theorem for robust parameter estimation, providing full posterior probability distributions.
* **Nested Sampling with `cpnest`:** Efficient computation of Bayesian evidences and accurate posterior distributions for complex likelihoods, particularly effective for high-dimensional parameter spaces.
* **Cosmological Model Exploration:** Implements and compares three different cosmological models (Flat, Closed, and Open Universes) by fitting key parameters (e.g., absolute magnitude `M`, matter density `Ω_M`, dark energy density `Ω_Λ`).
* **Numerical Integration of Cosmology:** Uses numerical methods (e.g., `np.trapz`) to solve the luminosity distance integral for different cosmological scenarios.
* **Uncertainty Quantification:** Robust estimation of parameter uncertainties, correlations, and credible intervals through analysis of posterior samples.
* **Scientific Computing & Domain Expertise:** Demonstrates proficiency in handling specialized scientific datasets and applying advanced computational tools within the field of observational cosmology.
* **Reproducible Analysis:** Code is provided in standalone Python scripts, designed for clear execution and analysis.

## Installation and Setup

This project requires a specific Python environment due to library compatibility, particularly with `cpnest`.

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone [https://github.com/vsbunny/data-science-portfolio.git](https://github.com/vsbunny/data-science-portfolio.git)
    cd data-science-portfolio/Observational_cosmology
    ```
    
2. **Install LaTeX Distribution (for plot rendering):**
    This project uses LaTeX for high-quality text rendering in plots (`matplotlib.rc('text', usetex=True)`). You will need a LaTeX distribution installed on your system.
    * **macOS:** Install [MacTeX](https://tug.org/mactex/).
    * **Linux:** Install [TeX Live](https://www.tug.org/texlive/) (e.g., `sudo apt-get install texlive-full` or `texlive-latex-extra`).
    * **Windows:** Install [MikTeX](https://miktex.org/download) or [TeX Live](https://www.tug.org/texlive/).

    After installation, ensure LaTeX commands are available in your system's PATH.
    
3.  **Create and activate a dedicated Python 3.7 virtual environment (highly recommended for `cpnest` compatibility):**
    * **Using `conda` (recommended for easier environment management):**
        ```bash
        conda create -n cpnest_env python=3.7
        conda activate cpnest_env
        ```
    * **Using `venv` (standard Python virtual environment):**
        ```bash
        python3.7 -m venv venv_cpnest
        source venv_cpnest/bin/activate
        ```

4.  **Install Python dependencies:**
    * First, ensure `pip` is updated within your new environment:
        ```bash
        python -m pip install --upgrade pip
        ```
    * Then, install project-specific requirements:
        ```bash
        pip install -r requirements.txt
        ```
        (Make sure you create a `requirements.txt` file in *this* `Observational_cosmology/` folder, listing all dependencies needed like `cpnest`, `numpy`, `astropy`, `corner`, etc.)

## Usage

To run the cosmological parameter estimation analysis for each model and generate plots:

1.  Ensure you have followed the [Installation and Setup](#installation-and-setup) steps.
2.  Activate your virtual environment (e.g., `conda activate cpnest_env`).
3.  **Run the cosmological model scripts:**
    Execute each model script from your terminal. This will run the `cpnest` sampling and save the posterior samples in their respective `Run_files_...` folders.
    ```bash
    python ObsCosNest_flat.py
    python ObsCosNest_open.py
    python ObsCosNest_closed.py
    ```
4.  **Generate Corner Plots:**
    After running the model scripts, execute the plotting script. This will load the posterior samples and save the corner plots to the `Corner_plots/` directory.
    ```bash
    python Cornerplot_flat.py
    python Cornerplot_open.py
    python Cornerplot_closed.py
    ```

## Results and Insights

This project successfully implemented Bayesian inference using `cpnest` to estimate cosmological parameters across three distinct cosmological models: Flat, Closed, and Open Universes. For each model, the `cpnest` sampler demonstrated effective exploration of the parameter space, with all runs showing good convergence to well-defined posterior distributions and generating posterior samples.

* **Flat Universe Model (Ω_m + Ω_Λ = 1):** The analysis constrained the absolute magnitude ($M$) and matter density ($\Omega_M$). The corner plot for this model shows clear, well-defined marginal distributions for these two independent parameters.
* **Closed Universe Model (Ω_m + Ω_Λ > 1):** This model constrained $M$, $\Omega_M$, and $\Omega_Λ$. The results exhibited strong negative correlations, particularly between $\Omega_M$ and $\Omega_Λ$, which is a common degeneracy observed in cosmological parameter fitting.
* **Open Universe Model (Ω_m + Ω_Λ < 1):** For this model, constraints were obtained for $M$, $\Omega_M$, and $\Omega_Λ$. The posterior distributions revealed a strong *positive* correlation between $\Omega_M$ and $\Omega_Λ$, a distinct feature for this model and dataset compared to the closed universe.

The generated corner plots (found in the `Corner_plots/` directory) visually represent these marginalized posterior distributions, illustrating parameter correlations and credible regions for each cosmological scenario. This work showcases the application of advanced sampling techniques for complex scientific problems and the ability to extract meaningful statistical insights from observational data.

## Future Work

* Explore more complex cosmological models or alternative likelihood functions (e.g., including neutrino mass, early dark energy).
* Integrate with larger datasets or actual observational data from ongoing surveys.
* Investigate different sampling algorithms within `cpnest` or other packages for comparison (e.g., `emcee`, `dynesty`).
* Implement custom plotting scripts for more specialized visualizations.

## Author

[Vanya Fernandez Galabo]