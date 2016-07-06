from .geom_boxplot import geom_boxplot
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class geom_errorbar(geom_boxplot):
    DEFAULT_PARAMS = {
        'outliers': False,
        'lines': True,
        'notch': True,
        'median': False,
        'box': False
    }
