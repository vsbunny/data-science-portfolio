#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Observational cosmology - fourth year assignment
Vanya

{This code fits low and high redshifts simultaneously, and treats CurlyM as a free parameter alongside Omega_M, and Omega_L}
There are three different codes for each case - omega_m + omega_L = 1, omega_m + omega_L >1, and omega_m +  omega_L <1. This will
make the corresponding corner plots for each case, and makes the calculation easier, instead of running if statements in the model function

- Modified on 17/05/2025
{Added a prior distribution for the parameters, removed cpnest.plot(), as another script is used for plotting. Requires Python = 3.7}
"""
#------------------------------------------------
#           omega_m +  omega_L > 1 (Closed Universe)
#------------------------------------------------
from __future__ import print_function, division
# Import print_function and division from the __future__ module.
# Ensures print behaves as a function and division results in a float.
from astropy.cosmology import WMAP9 as cosmo
# Import the WMAP9 cosmology model from astropy.cosmology.
# Provides cosmological parameters from WMAP 9-year data.
import os # Import the os module for path manipulation and directory creation
import sys
# Import the sys module for system-specific parameters and functions (not used here).
import numpy as np
# Import numpy for numerical computations and array handling.

# import CPNest
from cpnest.model import Model
# Import the Model class from cpnest.model.
# User-defined models inherit from this.
import cpnest
# Import the cpnest module for the CPNest sampler.

# import data
# import data
data = np.loadtxt('supernovae_data.dat') # Load data from 'supernovae_data.dat' using numpy.loadtxt().
# Assumes whitespace-separated columns: redshift, distance modulus, errors.
cosmo.H(0)      #Access the Hubble constant (H0) from the WMAP9 cosmology model.
# cosmo.H(0) evaluates the Hubble parameter at z=0, returning H0.
c = 299792.458 # Define the speed of light in km/s.


# Extract needed array from data file
z = data[:, 0]          # Extract redshift values from the first column (index 0) of 'data'.
sigmaz = data[:, 1]
meff = data[:, 7]       # Extract effective distance modulus from the eighth column (index 7) of 'data'.
sigmam = data[:, 8]     # Extract distance modulus errors from the ninth column (index 8) of 'data'.
sigma = np.mean(sigmam)     # Calculate the mean of the distance modulus errors.
LN2PI = np.log(2. * np.pi) # Pre-calculate ln(2π) for the Gaussian likelihood.
LNSIGMA = np.log(sigma)     # Pre-calculate ln(σ) for the Gaussian likelihood.


# Define the theoretical  cosmologies
def CosmologyModel(z, params):
    """
    Calculates the theoretical distance modulus for a given cosmology,
    assuming omega_L + omega_m > 1 (closed universe).

    Args:
        z (array_like): Array of redshifts.
        params (dict): Dictionary of cosmological parameters:
            {'CurlyM': ..., 'omega_m': ..., 'omega_L': ...}.

    Returns:
        array_like: Array of theoretical distance moduli.
    """
    CurlyM = params['CurlyM']       # Extract the absolute magnitude parameter.
    omega_m = params['omega_m']    # Extract the matter density parameter.
    omega_L = params['omega_L']    # Extract the dark energy density parameter.
    dz = 0.01  # Define the redshift spacing for the numerical integration.
    result = []  # Initialize an empty list to store the calculated distance moduli.
    k = omega_m + omega_L - 1  # Curvature parameter, ensures k > 0
    # Calculate the curvature parameter k, which is 1 - omega_m - omega_L for a closed universe.
    for zi in z:                        # Iterate over each redshift value in the input array z.
        z_array = np.arange(0, zi, dz) # Create an array of redshift values from 0 to the current redshift zi, with spacing dz

        # omega_L + omega_m > 1 # Removed: Handled by parameter bounds and likelihood
        # Calculate the integrand of the luminosity distance integral.  This integrand depends on the redshift, omega_m, and omega_L:
        integrand = ((1 + z_array) ** 2 * (1 + omega_m * z_array) - (z_array) * (2 + z_array) * omega_L) ** (-0.5)

        result.append((CurlyM + 5 * np.log10(c * (1 + zi) * np.arcsin(np.sqrt(k) * np.trapz(integrand, dx=dz)))) / np.sqrt(k))
    return result
# Defines the theoretical cosmology model for the case where omega_L + omega_m > 1.
# It calculates the distance modulus as a function of redshift and cosmological parameters,
# using numerical integration (trapezoidal rule) and accounting for the curvature.


# set the model, & likelihood function in order to estimate parameters
class ParamEstim(Model):
    """
    Defines the likelihood function and prior distribution for the parameters.
    """
    def __init__(self, names, bounds, data, modelfunc, sigma):
        """
        Initializes the ParamEstim model.

        Args:
            names (list): List of parameter names.
            bounds (list): List of parameter bounds [(lower, upper), ...].
            data (array_like): Observed distance modulus data (meff).
            modelfunc (callable): Function to calculate the theoretical distance modulus (CosmologyModel).
            sigma (float): Standard deviation of the distance modulus.
        """
        self._data = data           # Store the observed effective distance modulus data.
        self.bounds = bounds        # Store the bounds on the parameters being estimated.
        self.names = names          # Store the names of the parameters.
        self._sigma = sigma         # Store the standard deviation of the effective distance modulus.
        self._logsigma = np.log(sigma)  # Pre-calculate the log of sigma for use in the likelihood calculation.
        self._ndata = len(self._data)       # Store the number of data points.
        self._model = modelfunc         # Store the model function (CosmologyModel).


    def log_likelihood(self, livepoint):
        """
        Calculates the log-likelihood function.

        Args:
            livepoint (dict): Dictionary of parameter values.

        Returns:
            float: The log-likelihood value.
        """
        model = self._model(z, params=livepoint) # Calculate the theoretical distance modulus using CosmologyModel.
        norm = -0.5 * self._ndata * LN2PI - self._ndata * np.log(sigma)  # Calculate the normalization constant for the Gaussian likelihood.
        chisq = np.sum(((self._data - model) / (self._sigma)) ** 2)      # Calculate the chi-squared statistic.
        return norm - 0.5 * chisq

    def prior(self, x):
        """
        Defines the prior distribution for the parameters (uniform prior).

        Args:
            x (array_like): Vector of values in the range [0, 1].

        Returns:
            dict: Dictionary of parameter values transformed from the
                unit hypercube to the parameter space.
        """
        params = {}
        for i, name in enumerate(self.names):
            lower, upper = self.bounds[i]
            params[name] = lower + (upper - lower) * x[i]
        return params

# Define the names of the parameters to be estimated: CurlyM (absolute magnitude),
# omega_L (dark energy density), and omega_m (matter density).
names = ['CurlyM', 'omega_L', 'omega_m']

# Define bounds for each parameter
bounds = [
    [-3.5, -2],
    [-1, 1.5],
    [0, 1.5]
]


# Create an instance of the ParamEstim class, defining the model for CPNest.
mod = ParamEstim(names, bounds, meff, CosmologyModel, sigma)


# --- Define the output folder for CPNest results ---
# All CPNest output files (e.g., posterior samples, log files, evidence files)
# will be saved in this dedicated directory.
OUTPUT_FOLDER = "Run_files_closed" # Changed folder name for this specific case
# Create the directory if it doesn't exist
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
    print(f"Created output directory: {OUTPUT_FOLDER}")


# Settings for the sampler
cpnest_dict = {
    'nlive': 1024,       # 'nlive': Number of live points for the nested sampling algorithm.  Determines the exploration of the parameter space.
    'nthreads': 2,       # 'nthreads': Number of threads to use for parallel computation, speeding up the sampling process.
    'verbose': 3,        # Level of verbosity of the output: (0=silent, 1=progress, 2=diagnostic, 3=detailed)
    'output': OUTPUT_FOLDER, # 'output': Directory where CPNest will save its output files. Now points to the new folder.
    'resume': "resume",  # 'resume': "resume" to continue from a previous run, or another value (e.g., "new") to start a new run.
    'maxmcmc': 1024      # 'maxmcmc': Maximum length of the Markov Chain Monte Carlo (MCMC) chain used to sample within each nested sampling iteration.
}
# Define a dictionary of settings for the CPNest sampler.

if __name__ == '__main__':
    # Main execution block
    cpn = cpnest.CPNest(usermodel=mod, **cpnest_dict)
    # Create an instance of the CPNest class with the model and settings.  This sets up the
    # nested sampling run.

    cpn.run()
    # Run the CPNest sampler to perform the Bayesian parameter estimation.  This is where the
    # actual sampling and computation happen.

    # Save the posterior samples generated by CPNest. CPNest automatically saves this
    # inside the 'output' folder specified in cpnest_dict.
    cpn.get_posterior_samples(filename='posterior_closed.dat') # Filename within the output folder.
    # cpn.plot()  # Removed: Use external script for plotting.
    # The original code attempted to use CPNest's built-in plotting, but this has been removed
    # in favor of using a separate script that provides more customized plots.