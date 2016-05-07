from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import pandas as pd
from .ggplot import ggplot
from .stats import smoothers
from .stats import smoothers
from .utils import is_categorical


class geom(object):
    _aes_renames = {}
    DEFAULT_AES = {}

    def __init__(self, **kwargs):
        self.layers = [self]
        self.params = kwargs
        self.VALID_AES = set(list(self.DEFAULT_AES.keys()) + list(self.REQUIRED_AES) + list(self._aes_renames.values()))

    def __radd__(self, gg):
        if isinstance(gg, ggplot):
            gg.layers += self.layers
            # param_repr = ", ".join(["%s=%s" % (key, value) for key, value in self.params.items()])
            # gg._code.append("%s(%s)" % (type(self).__name__, param_repr))
            return gg

        self.layers.append(gg)
        return self

    def _rename_parameters(self, params):
        pass

    def _get_plot_args(self, data, _aes):
        variables = _aes.data
        params = {}

        for aes_type, default_value in self.DEFAULT_AES.items():
            # if we don't have an aesthetic for aes_type, add it to our params and set it to the default value
            if aes_type not in variables:
                params[aes_type] = default_value
            elif data[variables[aes_type]].nunique()==1:
                params[aes_type] = data[variables[aes_type]].iloc[0]
            else:
                params[aes_type] = data[variables[aes_type]]
            # else:
            #     # TODO: I can't remember why this is needed, but i think it's needed for pseudo-continuous data
            #     params[aes_type] = data[variables[aes_type]].iloc[0]

        params.update(self.params)
        for aes_type, mpl_param in self._aes_renames.items():
            if aes_type in variables:
                # TODO: what if it's a continuous number but there's only 1 datapoint in the segment
                if data[variables[aes_type]].nunique()==1:
                    params[mpl_param] = data[variables[aes_type]].iloc[0]
                else:
                    params[mpl_param] = data[variables[aes_type]]
            # maybe this should be an elif?
            if aes_type in params:
                params[mpl_param] = params[aes_type]
                del params[aes_type]

        valid_params = {}
        for key, value in params.items():
            if key not in self.VALID_AES:
                continue
            valid_params[key] = value

        return valid_params

class geom_point(geom):
    DEFAULT_AES = {'alpha': 1, 'color': 'black', 'shape': 'o', 'size': 20, 'edgecolors': None}
    REQUIRED_AES = {'x', 'y'}
    _aes_renames = {'size': 's', 'shape': 'marker', 'color': 'c'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
        x = data[variables['x']]
        y = data[variables['y']]

        params = self._get_plot_args(data, _aes)

        if 'colormap' in variables:
            params['cmap'] = variables['colormap']

        ax.scatter(x, y, **params)

class geom_area(geom):

    DEFAULT_AES = {'alpha': None, 'color': None, 'fill': '#333333',
                   'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'x', 'ymax', 'ymin'}
    DEFAULT_PARAMS = {'stat': 'identity', 'position': 'stack'}

    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth', 'fill': 'facecolor', 'color': 'edgecolor'}
    def plot(self, ax, data, _aes):
        variables = _aes.data
        x = data[variables['x']]
        ymin = data[variables['ymin']]
        ymax = data[variables['ymax']]

        # TODO: for some reason the reordering produces NaNs
        order = x.argsort()

        params = self._get_plot_args(data, _aes)
        ax.fill_between(x, ymin, ymax, **params)

class geom_line(geom):
    DEFAULT_AES = {'color': 'black', 'alpha': 1.0, 'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'x', 'y'}
    DEFAULT_PARAMS = {'stat': 'identity', 'position': 'identity'}

    _aes_renames = {'size': 'linewidth', 'linetype': 'linestyle'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
        x = data[variables['x']]
        y = data[variables['y']]

        params = self._get_plot_args(data, _aes)
        ax.plot(x, y, **params)


class geom_boxplot(geom):
    DEFAULT_AES = {'y': None, 'color': 'black', 'flier_marker': '+'}
    REQUIRED_AES = {'x'}
    DEFAULT_PARAMS = {'stat': 'identity', 'position': 'identity'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
        x = data[variables['x']]
        params = self._get_plot_args(data, _aes)

        q = ax.boxplot(x, vert=True)
        plt.setp(q['boxes'], color=params['color'])
        plt.setp(q['whiskers'], color=params['color'])
        plt.setp(q['fliers'], color=params['color'])


class geom_blank(geom):

    def plot(self, ax, data, _aes):
        variables = _aes.data
        pass

class geom_histogram(geom):

    DEFAULT_AES = {'alpha': None, 'color': None, 'fill': '#333333',
                   'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'x'}
    DEFAULT_PARAMS = {'stat': 'bin', 'position': 'stack'}
    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth',
                    'fill': 'color', 'color': 'edgecolor'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
        x = data[variables['x']]
        params = self._get_plot_args(data, _aes)
        ax.hist(x, **params)

class geom_density(geom):

    DEFAULT_AES = {'alpha': None, 'color': 'black',
                   'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'x'}
    DEFAULT_PARAMS = {'stat': 'density', 'position': 'identity'}

    _extra_requires = {'y'}
    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth'}

    def _calculate_density(self, x):
        kde = gaussian_kde(x)
        bottom = np.min(x)
        top = np.max(x)
        step = (top - bottom) / 1000.0

        x = np.arange(bottom, top, step)
        y = kde.evaluate(x)
        return x, y

    def plot(self, ax, data, _aes):
        variables = _aes.data
        x = data[variables['x']]
        x, y = self._calculate_density(x)
        params = self._get_plot_args(data, _aes)
        ax.plot(x, y, **params)

class geom_abline(geom):

    DEFAULT_AES = {'color': 'black', 'linetype': 'solid',
                   'alpha': None, 'size': 1.0, 'x': None,
                   'y': None}
    REQUIRED_AES = {'slope', 'intercept'}
    DEFAULT_PARAMS = {'stat': 'abline', 'position': 'identity'}

    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth'}

    def plot(self, ax, data, _aes):
        variables = _aes.data

        slope = self.params.get('slope', 1)
        intercept = self.params.get('intercept', 0)

        x = ax.get_xticks()
        y = ax.get_xticks() * slope + intercept
        params = self._get_plot_args(data, _aes)
        # don't need the original params from the aesthetics
        del params['x']
        del params['y']
        del params['slope']
        del params['intercept']
        ax.plot(x, y, **params)


class geom_hline(geom):
    DEFAULT_AES = {'color': 'black', 'linetype': 'solid',
                   'size': 1.0,}
    REQUIRED_AES = {'yintercept'}
    DEFAULT_PARAMS = {'stat': 'hline', 'position': 'identity',
                      'show_guide': False}

    _aes_renames = {'size': 'linewidth', 'linetype': 'linestyle'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
        y = self.params.get('y')
        params = self._get_plot_args(data, _aes)
        ax.axhline(y, **params)

class geom_vline(geom):

    DEFAULT_AES = {'color': 'black', 'linetype': 'solid',
                   'size': 1.0}
    REQUIRED_AES = {'xintercept'}
    DEFAULT_PARAMS = {'stat': 'vline', 'position': 'identity',
                      'show_guide': False}
    _aes_renames = {'size': 'linewidth', 'linetype': 'linestyle'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
        x = self.params.get('x')
        params = self._get_plot_args(data, _aes)
        ax.axvline(x, **params)

class geom_bar(geom):

    DEFAULT_AES = {'alpha': None, 'color': None, 'fill': '#333333',
                   'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'x'}
    DEFAULT_PARAMS = {'stat': 'bin', 'position': 'stack'}
    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth',
                    'fill': 'color', 'color': 'edgecolor'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
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

        params = self._get_plot_args(data, _aes)
        params.update(self.params)

        ax.bar(left, heights, width, **params)

        if categorical:
            ax.set_xticks(left+width/2)
            ax.set_xticklabels(x)

class stat_smooth(geom):

    DEFAULT_PARAMS = {'geom': 'smooth', 'position': 'identity', 'method': 'auto',
            'se': True, 'n': 80, 'fullrange': False, 'level': 0.95,
            'span': 2/3., 'window': None}
    REQUIRED_AES = {'x', 'y'}
    _aes_renames = {'size': 'linewidth', 'linetype': 'linestyle'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
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

        params = self._get_plot_args(data, _aes)
        if 'alpha' not in params:
            params['alpha'] = 0.2

        order = np.argsort(x)
        if self.params.get('se', True)==True:
            ax.fill_between(x[order], y1[order], y2[order], **params)
        if self.params.get('fit', True)==True:
            del params['alpha']
            ax.plot(x[order], y[order], **params)

stat_density = geom_density
