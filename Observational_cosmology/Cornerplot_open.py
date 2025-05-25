# --- Corner Plot for ObsCosNest_open.py - Open Universe Model --- 
import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
import os # Import the os module for path manipulation

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
INPUT_DATA_FOLDER = "Run_files_open"

# --- Define the Posterior Sample Filename ---
# This matches the filename specified in cpn.get_posterior_samples(filename='posterior2.dat') for this model.
POSTERIOR_FILENAME = "posterior_open.dat" 


# --- Data Loading ---
# Construct the full path to the posterior samples file.
data_path = os.path.join(INPUT_DATA_FOLDER, POSTERIOR_FILENAME)
# Load data from the specified path.
# skiprows=1: Skips the first row (e.g., a header row from CPNest).
# usecols=(0,1,2): Reads data only from columns 0, 1, and 2, which correspond to
# the CurlyM, omega_L, and omega_m parameters respectively, as defined in the CPNest model.
data = np.loadtxt(data_path, skiprows=1, usecols = (0,1,2))

"""
source={'t_start': 5.,
        'log_amplitude': -38.,
        'damp_tau': .01,
        'mode_frequency': 200.,
        'phase': 2.}
"""

# --- Define Output Folder for Plots ---
# It's good practice to organize output plots into a dedicated directory.
OUTPUT_PLOT_FOLDER = "Corner_plots"
# Check if the output directory exists, and create it if it doesn't.
if not os.path.exists(OUTPUT_PLOT_FOLDER):
    os.makedirs(OUTPUT_PLOT_FOLDER)
    print(f"Created output directory for plots: {OUTPUT_PLOT_FOLDER}")


# --- Produce a Corner Plot ---
# The 'corner.corner' function creates a corner plot from the posterior samples.
# This plot shows the 1D marginalized probability distributions (histograms) for each parameter
# along the diagonal, and 2D marginalized probability distributions (scatter plots/contours)
# for each pair of parameters off-diagonal.
figure = corner.corner(data,
                        labels=[r"$M$", r"$\Omega_{\lambda}$", r"$\Omega_M$"], # LaTeX labels for parameters
                        title_fmt='.4f',       # Format string for title values (e.g., median and uncertainties)
                        quantiles=[0.16, 0.5, 0.84], # Quantiles to compute and show on 1D histograms
                        show_titles=True,      # Display titles with median and uncertainty for each parameter
                        )

# --- Save the Corner Plot ---
# Save the generated corner plot to a PNG file within the specified output folder.
# The filename includes the folder path.
plt.savefig(os.path.join(OUTPUT_PLOT_FOLDER, 'cornerplot_open.png'))

print(f"Corner plot saved to: {os.path.join(OUTPUT_PLOT_FOLDER, 'cornerplot_open.png')}")

# Note: plt.show() is not called because matplotlib.use('Agg') prevents GUI display.
# The plot is saved directly to a file.