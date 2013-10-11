import matplotlib.pyplot as plt
from copy import deepcopy
from geom import geom
import pandas as pd
import numpy as np
from ggplot.components import smoothers

class stat_smooth(geom):
    VALID_AES = ['x', 'y', 'color', 'alpha', 'label', 'se', 'method', 'span']

    def plot_layer(self, layer):
        layer = {k: v for k, v in layer.iteritems() if k in self.VALID_AES}
        layer.update(self.manual_aes)

        if 'x' in layer:
            x = layer.pop('x')
        if 'y' in layer:
            y = layer.pop('y')
        if 'se' in layer:
            se = layer.pop('se')
        else:
            se = None
        if 'span' in layer:
            span = layer.pop('span')
        else:
            span = 2/3.
        if 'method' in layer:
            method = layer.pop('method')
        else:
            method = None

        if method == "lm":
            y, y1, y2 = smoothers.lm(x, y)
        elif method == "ma":
            y, y1, y2 = smoothers.mavg(x, y)
        else:
            y, y1, y2 = smoothers.lowess(x, y)
        idx = np.argsort(x)
        x = np.array(x)[idx]
        y = np.array(y)[idx]
        y1 = np.array(y1)[idx]
        y2 = np.array(y2)[idx]
        plt.plot(x, y, **layer)
        if se==True:
            plt.fill_between(x, y1, y2, alpha=0.2, color="grey")
