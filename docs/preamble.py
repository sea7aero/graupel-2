# +
"""
This python module is intended to be included in each notebook and defines a bunch of common things for all of them.
"""
import math
import numpy as np
import pandas as pd

import pint
units = pint.UnitRegistry()

from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

sns.set_theme()
sns.set_style("ticks")

plt.rcParams['figure.figsize'] = (16, 5)
plt.rcParams['figure.dpi']= 150

# Show ticks every 15 minutes.
locator = mdates.MinuteLocator(byminute=[0,15,30,45])
formatter = mdates.ConciseDateFormatter(locator)

def pretty_plots(nrows=1, ncols=1):
    fig, ax = plt.subplots(nrows, ncols, tight_layout=True)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    return ax
# -


