from .geom_boxplot import geom_boxplot
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class geom_errorbar(geom_boxplot):
    """
    Error bar plot

    Parameters
    ----------
    x:
        x values for (x, y) coordinates
    y:
        value to calculate error ranges for
    color:
        color of line
    flier_marker:
        type of marker used ('o', '^', 'D', 'v', 's', '*', 'p', '8', "_", "|", "_")

    Examples
    --------
    """
    DEFAULT_PARAMS = {
        'outliers': False,
        'lines': True,
        'notch': True,
        'median': False,
        'box': False
    }
