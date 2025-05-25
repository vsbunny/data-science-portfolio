# --- Corner Plot for ObsCosNest_flat.py - Flat Universe Model --- 
import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
import os # Import os for path manipulation

import corner

# Change to LaTeX fonts:
from matplotlib import rc
rc('font',**{'family':'serif','sans-serif':['Computer Modern Roman']})
rc('text', usetex=True)

# Adjust label sizes
plt.rcParams.update({'font.size': 11})
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8

# --- Define Input Data Folder ---
INPUT_DATA_FOLDER = "Run_files_flat" # For the flat model case
POSTERIOR_FILENAME = "posterior_flat.dat" # Filename for flat model posterior

# --- Data Loading ---
data_path = os.path.join(INPUT_DATA_FOLDER, POSTERIOR_FILENAME)
# Load data: Now only load the two sampled parameters (CurlyM and omega_m)
# Column 0 is CurlyM, Column 1 is omega_m
data = np.loadtxt(data_path, skiprows=1, usecols = (0,1)) 

# --- Produce a Corner Plot (Corrected Labels for Flat Model) ---
# This section generates the corner plot from the posterior samples.
# For the flat universe model (where Ω_m + Ω_Λ = 1), CPNest samples only two independent parameters:
# CurlyM (absolute magnitude) and Ω_M (matter density). Ω_Λ is then a derived parameter (1 - Ω_M).
# The plot therefore visualizes the 1D and 2D marginalized posterior distributions for these
# two independently sampled parameters.
figure = corner.corner(data,
                        labels=[r"$M$", r"$\Omega_M$"], # Labels for the two independently sampled parameters
                        title_fmt='.4f',                # Format string for titles (median and uncertainties)
                        quantiles=[0.16, 0.5, 0.84],    # Quantiles to compute and show on 1D histograms (68% credible interval)
                        show_titles=True,               # Display titles with median and uncertainty for each parameter
                        )

Sources

# --- Define Output Folder for Plots ---
OUTPUT_PLOT_FOLDER = "Corner_plots"
if not os.path.exists(OUTPUT_PLOT_FOLDER):
    os.makedirs(OUTPUT_PLOT_FOLDER)
    print(f"Created output directory for plots: {OUTPUT_PLOT_FOLDER}")


plt.savefig(os.path.join(OUTPUT_PLOT_FOLDER, 'cornerplot_flat.png'))

print(f"Corner plot saved to: {os.path.join(OUTPUT_PLOT_FOLDER, 'cornerplot_flat.png')}")