import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ggplot import ggplot
from aes import aes
from stats import smoothers
import utils
from utils import is_categorical


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

        if 'colormap' in variables:
            params['cmap'] = variables['colormap']

        ax.scatter(x, y, **params)

class geom_area(geom):

    def plot(self, ax, data, variables):
        x = data[variables['x']]
        ymin = data[variables['ymin']]
        ymax = data[variables['ymax']]
        order = x.argsort()
        params = {}
        # TODO: for some reason the reordering produces NaNs
        ax.fill_between(x, ymin, ymax)

class geom_line(geom):

    def plot(self, ax, data, variables):
        x = data[variables['x']]
        y = data[variables['y']]
        ax.plot(x, y)

class geom_blank(geom):

    def plot(self, ax, data, variables):
        pass

class geom_histogram(geom):

    def plot(self, ax, data, variables):
        x = data[variables['x']]
        ax.hist(x)

class geom_density(geom):

    def plot(self, ax, data, variables):
        x = data[variables['x']]
        sns.distplot(x, hist=False, kde=True)

class geom_abline(geom):

    "intercept, slope"

    def plot(self, ax, data, variables):

        slope = self.params.get('slope', 1)
        intercept = self.params.get('intercept', 0)

        x = ax.get_xticks()
        y = ax.get_xticks() * slope + intercept

        ax.plot(x, y)


class geom_hline(geom):

    def plot(self, ax, data, variables):
        ax.axhline(self.params.get('y'))

class geom_vline(geom):

    def plot(self, ax, data, variables):
        ax.axvline(self.params.get('x'))

class geom_bar(geom):

    def plot(self, ax, data, variables):
        x = data[variables['x']]
        weight = variables.get('weight')
        if weight:
            cols = [variables['x'], variables['weight']]
            xdata = data[cols].groupby(variables['x']).sum().reset_index()
            x = xdata[variables['x']]
            heights = xdata['x']
        else:
            xdata = x.value_counts().reset_index()
            x = xdata['index']
            heights = xdata[variables['x']]

        categorical = is_categorical(x)

        width_elem = self.params.get('width')
        # If width is unspecified, default is an array of 1's
        if width_elem == None:
            width = np.ones(len(x))
        else :
            width = np.array(width_elem)

        # layout and spacing
        #
        # matplotlib needs the left of each bin and it's width
        # if x has numeric values then:
        #   - left = x - width/2
        # otherwise x is categorical:
        #   - left = cummulative width of previous bins starting
        #            at zero for the first bin
        #
        # then add a uniform gap between each bin
        #   - the gap is a fraction of the width of the first bin
        #     and only applies when x is categorical
        _left_gap = 0
        _spacing_factor = 0     # of the bin width
        if not categorical:
            left = np.array([x[i]-width[i]/2 for i in range(len(x))])
        else:
            _left_gap = 0.2
            _spacing_factor = 0.105     # of the bin width
            _breaks = np.append([0], width)
            left = np.cumsum(_breaks[:-1])
        _sep = width[0] * _spacing_factor
        left = left + _left_gap + [_sep * i for i in range(len(left))]

        ax.bar(left, heights, width, **self.params)

        if categorical:
            ax.set_xticks(left+width/2)
            ax.set_xticklabels(x)

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
