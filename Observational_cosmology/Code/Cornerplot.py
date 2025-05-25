import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

import corner

# Change to LaTeX fonts:
from matplotlib import rc
rc('font',**{'family':'serif','sans-serif':['Computer Modern Roman']})
rc('text', usetex=True)

# Adjust label sizes
plt.rcParams.update({'font.size': 11})
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8

# Load data
data = np.loadtxt('posterior.dat', skiprows=1, usecols = (0,1,2))

# True source values
"""
source={'t_start': 5.,
        'log_amplitude': -38.,
        'damp_tau': .01,
        'mode_frequency': 200.,
        'phase': 2.}
"""
# Produce a corner plot
figure = corner.corner(data,
        					  labels=[r"$M$", r"$\Omega_{\lambda}$", r"$\Omega_M$"],
                       title_fmt='.4f',
                       quantiles=[0.16, 0.5, 0.84],
                       show_titles=True,
                       )

plt.savefig('cornermodified.png')
