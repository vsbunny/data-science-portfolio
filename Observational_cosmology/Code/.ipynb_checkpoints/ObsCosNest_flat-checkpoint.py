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
#           omega_m +  omega_L = 1 (Flat Model)
#------------------------------------------------
from __future__ import print_function, division
# Import print_function and division from the __future__ module.
# This ensures that print behaves as a function in Python 2 and 3,
# and that division always results in a float.
from astropy.cosmology import WMAP9 as cosmo
# Import the WMAP9 cosmology model from astropy.cosmology.
# This provides cosmological parameters (like the Hubble constant)
# from the Wilkinson Microwave Anisotropy Probe (WMAP) 9-year data.
import numpy as np
# Import numpy for numerical computations and array handling.

# import CPNest
from cpnest.model import Model
# Import the Model class from cpnest.model.
# User-defined models (like ParamEstim) inherit from this.
import cpnest
# Import the cpnest module for the CPNest sampler.

# Load data
data = np.loadtxt('data.dat')
# Load data from 'data.dat' using numpy.loadtxt().
# Assumes whitespace-separated columns with redshift, distance modulus, and errors.
cosmo.H(0)      #using astropy to extract H(0)
# Access the Hubble constant (H0) from the WMAP9 cosmology model.
# cosmo.H(0) evaluates the Hubble parameter at z=0, effectively returning H0.
c = 299792.458 #speed of light in vacuum in km/s
# Define the speed of light in km/s.

# Extract needed array from data file
z = data[:, 0]         # Redshift data
# Extract redshift values from the first column (index 0) of 'data'.
sigmaz = data[:, 1]
meff = data[:, 7]       # Effective distance modulus
# Extract effective distance modulus from the eighth column (index 7) of 'data'.
sigmam = data[:, 8]     # Error in distance modulus
# Extract distance modulus errors from the ninth column (index 8) of 'data'.
sigma = np.mean(sigmam)  # Mean error
# Calculate the mean of the distance modulus errors.

# Define natural log of 2pi, and sigma needed for likelihood function
LN2PI = np.log(2. * np.pi)
# Pre-calculate ln(2π) for the Gaussian likelihood.
LNSIGMA = np.log(sigma)
# Pre-calculate ln(σ) for the Gaussian likelihood.


# Define the theoretical cosmologies
def CosmologyModel(z, params):
    """
    Calculates the theoretical distance modulus for a given cosmology.

    Args:
        z (array_like): Array of redshifts.
        params (dict): Dictionary of cosmological parameters
            {'CurlyM': ..., 'omega_m': ..., 'omega_L': ...}.

    Returns:
        array_like: Array of theoretical distance moduli.
    """
    CurlyM = params['CurlyM']
    omega_m = params['omega_m']
    omega_L = params['omega_L']
    dz = 0.01  # Redshift spacing for integration
    result = []  # Array to store results

    for zi in z:
        z_array = np.arange(0, zi, dz)
        # omega_L + omega_m == 1  # Removed: This is handled by the parameter bounds and likelihood 
        integrand = ((1 + z_array) ** 2 * (1 + omega_m * z_array) - (z_array) * (2 + z_array) * omega_L) ** (-0.5)
        result.append(CurlyM + 5 * np.log10(c * (1 + zi) * np.trapz(integrand, dx=dz)))
    return result
# Defines the theoretical cosmology model, calculating the distance modulus as a function of redshift
# and cosmological parameters.  It assumes a flat cosmology (omega_m + omega_L = 1) and uses numerical
# integration (trapezoidal rule) to compute the luminosity distance.


# Set the likelihood function
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
        self._ndata = len(self._data)   # Store the number of data points.        
        self._model = modelfunc         # Store the model function (CosmologyModel).
        

    def log_likelihood(self, livepoint):
        """
        Calculates the log-likelihood function.

        Args:
            livepoint (dict): Dictionary of parameter values at a given point
                in the parameter space.

        Returns:
            float: The log-likelihood value.
        """
        model = self._model(z, params=livepoint)
        # Calculate the theoretical distance modulus using the CosmologyModel.
        norm = -0.5 * self._ndata * LN2PI - self._ndata * np.log(sigma)
        # Calculate the normalization constant for the Gaussian likelihood.
        chisq = np.sum(((self._data - model) / (self._sigma)) ** 2)
        # Calculate the chi-squared statistic.
        print(chisq)
        return norm - 0.5 * chisq
    # Defines the log-likelihood function for the model.  Assumes Gaussian errors on the distance modulus
    # and calculates the likelihood of the observed data given the model and parameters.
    # 'livepoint' contains the parameter values being sampled.

    def prior(self, x):
        """
        Defines the prior distribution for the parameters (uniform prior).

        Args:
            x (array_like): Vector of values in the range [0, 1] representing
                the position in the unit hypercube.

        Returns:
            dict: Dictionary of parameter values transformed from the unit
                hypercube to the parameter space.
        """
        params = {}
        for i, name in enumerate(self.names):
            lower, upper = self.bounds[i]
            params[name] = lower + (upper - lower) * x[i]
        return params
    # Defines the prior distribution for the parameters.  A uniform prior is assumed within the parameter
    # bounds.  The input 'x' is a vector of values between 0 and 1, which are mapped to the
    # parameter ranges.


# Define the names of the parameters to be estimated: CurlyM (absolute magnitude),
# omega_L (dark energy density), and omega_m (matter density).
names = ['CurlyM', 'omega_L', 'omega_m']


# Define the bounds on each parameter
bounds = [
    [-3.5, -2],  # Bounds on CurlyM
    [-2, 2],     # Bounds on omega_L
    [0, 2]       # Bounds on omega_m (omega_m < 0 is unphysical)
]



# Set up the cpnest model
mod = ParamEstim(names, bounds, meff, CosmologyModel, sigma)
# Create an instance of the ParamEstim class, defining the model for CPNest.

# Settings for the sampler
cpnest_dict = {          # Define a dictionary of settings for the CPNest sampler.
    'nlive': 1024,       # 'nlive': Number of live points for the nested sampling.
    'nthreads': 2,       # 'nthreads': Number of threads for parallel computation; Number of parallel samplers
    'verbose': 3,        # Level of Verbosity (0=silent, 1=progress, 2=diagnostic, 3=detailed)
    'output': "./",      # 'output': Directory for output files.
    'resume': "resume",  # 'resume': "resume" to continue a previous run.
    'maxmcmc': 1024      # 'maxmcmc': Maximum length of the MCMC chain.
}


if __name__ == '__main__':
    # Main execution block
    cpn = cpnest.CPNest(usermodel=mod, **cpnest_dict)
    # Create an instance of the CPNest class with the model and settings.

    cpn.run()
    # Run the CPNest sampler.

    cpn.get_posterior_samples(filename='posterior.dat')
    # Save the posterior samples to 'posterior.dat'.
    # cpn.plot()  # Removed: Use external script for plotting.
