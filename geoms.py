import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ggplot import ggplot
from aes import aes
from stats import smoothers
import utils


class facet_wrap(object):
    def __init__(self, x=None, y=None):
        self.x_var = x
        self.y_var = y

    def __radd__(self, other):
        if isinstance(other, ggplot):
            other.grid = sns.FacetGrid(other.data, col=self.y_var,  row=self.x_var)
            return other

        return self

class geom(object):
    _aes_renames = {}

    def __init__(self, **kwargs):
        self.layers = [self]
        self.params = kwargs

    def __radd__(self, other):
        if isinstance(other, ggplot):
            other.layers += self.layers
            return other

        self.layers.append(other)
        return self

    def _get_plot_args(self, aes_map):
        args = {}
        for key, value in self._aes_renames.items():
            if key in aes_map:
                args[value] = aes_map[key]
            if key in self.params:
                args[value] = self.params[key]
        return args

class geom_point(geom):

    _aes_renames = {'size': 's', 'shape': 'marker', 'color': 'c'}

    def plot(self, ax, data, variables):
        x = data[variables['x']]
        y = data[variables['y']]

        params = {}
        for aes_type, mpl_param in self._aes_renames.items():
            if aes_type in variables:
                if data[variables[aes_type]].nunique()==1:
                    params[mpl_param] = data[variables[aes_type]].iloc[0]
                else:
                    params[mpl_param] = data[variables[aes_type]]

        ax.scatter(x, y, **params)

    def grid(self, ax, variables):
        ax.scatter(variables['x'], variables['y'])

class geom_line(geom):

    def plot(self, ax, data, variables):
        x = data[variables['x']]
        y = data[variables['y']]
        ax.plot(x, y)

    def grid(self, ax, variables):
        ax.plot(variables['x'], variables['y'])

class geom_hist(geom):

    def plot(self, ax, data, variables):
        x = data[variables['x']]
        ax.hist(x)

class geom_density(geom):

    def plot(self, ax, data, variables):
        x = data[variables['x']]
        sns.distplot(x, hist=False, kde=True)

class geom_abline(geom):
    # harder than it seems...
    pass

class geom_hline(geom):

    def plot(self, ax, data, variables):
        ax.axhline(self.params.get('y'))

class geom_vline(geom):

    def plot(self, ax, data, variables):
        ax.axvline(self.params.get('x'))


class stat_smooth(geom):

    def plot(self, ax, data, variables):
        x = data[variables['x']]
        y = data[variables['y']]

        params = {'alpha': 0.2}

        method = self.params.get('method', 'lm')
        level = self.params.get('level', 0.95)
        window = self.params.get('window', None)
        span = self.params.get('span', 2/3.)

        if method == "lm":
            x, y, y1, y2 = smoothers.lm(x, y, 1-level)
        elif method == "ma":
            x, y, y1, y2 = smoothers.mavg(x, y, window=window)
        else:
            x, y, y1, y2 = smoothers.lowess(x, y, span=span)

        order = np.argsort(x)
        if self.params.get('se', True)==True:
            ax.fill_between(x[order], y1[order], y2[order], **params)
        if self.params.get('fit', True)==True:
            ax.plot(x[order], y[order])
