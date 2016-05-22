from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
import datetime
from scipy.stats import gaussian_kde
from .ggplot import ggplot
from .stats import smoothers
from .stats import smoothers
from .utils import is_categorical, is_iterable
import datetime

date_types = (
    pd.tslib.Timestamp,
    pd.DatetimeIndex,
    pd.Period,
    pd.PeriodIndex,
    datetime.datetime,
    datetime.time
)
_isdate = lambda x: isinstance(x, date_types)

def _calc_n_bins(series):
    "https://en.wikipedia.org/wiki/Histogram#Number_of_bins_and_width"
    q75, q25 = np.percentile(series, [75 , 25])
    iqr = q75 - q25
    h = (2 * iqr) / (len(series)**(1/3.))
    k = (series.max() - series.min()) / h
    return k


class geom(object):
    _aes_renames = {}
    DEFAULT_AES = {}
    REQUIRED_AES = {}

    def __init__(self, **kwargs):
        self.layers = [self]
        self.params = kwargs

        self.VALID_AES = set()
        self.VALID_AES.update(self.DEFAULT_AES.keys())
        self.VALID_AES.update(self.REQUIRED_AES)
        self.VALID_AES.update(self._aes_renames.keys())

    def __radd__(self, gg):
        if isinstance(gg, ggplot):
            gg.layers += self.layers
            return gg

        self.layers.append(gg)
        return self

    def _rename_parameters(self, params):
        pass

    def _get_plot_args(self, data, _aes):
        mpl_params = {}
        mpl_params.update(self.DEFAULT_AES)

        # for non-continuous values (i.e. shape), need to only pass 1 value
        # into matplotlib. for example instead if ['+', '+', '+', ..., '+'] you'd
        # want to pass in '+'
        for key, value in _aes.items():
            if value not in data:
                mpl_params[key] = value
            elif data[value].nunique()==1:
                mpl_params[key] = data[value].iloc[0]
            else:
                mpl_params[key] = data[value]

        # parameters passed to the geom itself override the aesthetics
        mpl_params.update(self.params)

        items = list(mpl_params.items())
        for key, value in items:
            if key not in self.VALID_AES:
                del mpl_params[key]
            elif key in self._aes_renames:
                new_key = self._aes_renames[key]
                mpl_params[new_key] = value
                del mpl_params[key]


        for req in self.REQUIRED_AES:
            if req not in mpl_params:
                raise Exception("%s needed for %s" % (req, str(self)))
            else:
                del mpl_params[req]

        return mpl_params

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

        if self.params.get("jitter"):
            x *= np.random.uniform(.9, 1.1, len(x))
            y *= np.random.uniform(.9, 1.1, len(y))

        date_types = (
            pd.tslib.Timestamp,
            pd.DatetimeIndex,
            pd.Period,
            pd.PeriodIndex,
            datetime.datetime,
            datetime.time
        )
        if isinstance(x.iloc[0], date_types):
            # TODO: make this work for plot_date params
            ax.plot_date(x, y, **{})
        else:
            ax.scatter(x, y, **params)

class geom_jitter(geom_point):
    def __init__(self, *args, **kwargs):
        super(geom_point, self).__init__(*args, **kwargs)
        self.params['position'] = "jitter"

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
        # x value in fill_between can't be a date
        if _isdate(x.iloc[0]):
            dtype = x.iloc[0].__class__
            x = np.array([i.toordinal() for i in x])
            ax.fill_between(x, ymin, ymax, **params)
            new_ticks = [dtype(i) for i in ax.get_xticks()]
            ax.set_xticklabels(new_ticks)
        else:
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
        if 'slope' in params:
            del params['slope']
        if 'intercept' in params:
            del params['intercept']
        ax.plot(x, y, **params)


class geom_hline(geom):
    DEFAULT_AES = {'color': 'black', 'linetype': 'solid',
                   'size': 1.0,}
    REQUIRED_AES = {}
    DEFAULT_PARAMS = {'stat': 'hline', 'position': 'identity',
                      'show_guide': False}

    _aes_renames = {'size': 'linewidth', 'linetype': 'linestyle'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
        y = self.params.get('y')
        params = self._get_plot_args(data, _aes)
        if is_iterable(y):
            for yi in y:
                ax.axhline(yi, **params)
        else:
            ax.axhline(y, **params)

class geom_vline(geom):

    DEFAULT_AES = {'color': 'black', 'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {}
    DEFAULT_PARAMS = {'stat': 'vline', 'position': 'identity',
                      'show_guide': False}
    _aes_renames = {'size': 'linewidth', 'linetype': 'linestyle'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
        x = self.params.get('x')
        params = self._get_plot_args(data, _aes)

        if is_iterable(x):
            for xi in x:
                ax.axvline(xi, **params)
        else:
            ax.axvline(x, **params)


class geom_bar(geom):

    DEFAULT_AES = {'alpha': None, 'color': None, 'fill': '#333333',
                   'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'x'}
    DEFAULT_PARAMS = {'stat': 'bin', 'position': 'stack'}
    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth',
                    'fill': 'color', 'color': 'edgecolor'}

    def setup_data(self, data, _aes, facets=None):
        x_col = _aes['x']
        weight_col = _aes.get('weight')

        if not weight_col:
            if '__weight__' not in data:
                data.insert(0, '__weight__', 1)
            weight_col = '__weight__'
        else:
            data['__weight__'] = data[weight_col]
            weight_col = '__weight__'

        fill_col = _aes.get('fill')
        if not fill_col:
            return

        groupers = [x_col]
        if facets:
            if facets.rowvar:
                groupers.append(facets.rowvar)
            if facets.colvar:
                groupers.append(facets.colvar)
        dfa = (data[groupers + [fill_col, weight_col]].groupby(groupers + [fill_col]).sum()).reset_index()
        dfb = (data[groupers + [weight_col]].groupby(groupers).sum()).reset_index()
        df = pd.merge(dfa, dfb, on=groupers)
        df.rename(columns={'__weight___x': '__weight__', '__weight___y': '__total_weight__'}, inplace=True)
        if self.params.get('position')=='fill':
            df['__calc_weight__'] = df['__weight__'] / df['__total_weight__']
        else:
            df['__calc_weight__'] = df['__weight__']
        return df


    def plot(self, ax, data, _aes, x_levels, fill_levels, lookups):
        variables = _aes.data
        weight_col = _aes.get('weight')
        x_levels = sorted(x_levels)

        if not weight_col:
            if '__weight__' not in data:
                data.insert(0, '__weight__', 1.0)
            weight_col = '__weight__'

        params = self._get_plot_args(data, _aes)

        if self.params.get('position')=='fill':
            pass

        if fill_levels is not None:
            width = .8 / len(fill_levels)
        else:
            width = .8
        padding = width / 2


        xticks = []
        for i, x_level in enumerate(x_levels):
            mask = data[variables['x']]==x_level
            row = data[mask]
            if len(row)==0:
                xticks.append(i)
                continue

            if fill_levels is not None:
                fillval = row[variables['fill']].iloc[0]
                fill_idx = fill_levels.tolist().index(fillval)
                fill_x_adjustment = width * len(fill_levels)/2.
            else:
                fill_x_adjustment = width / 2

            if self.params.get('position') in ('stack', 'fill'):
                dodge = 0.0
                fill_x_adjustment = width / 2
                if fill_levels is None:
                    height = 1.0
                    ypos = 0
                else:
                    mask = (lookups[variables['x']]==x_level) & (lookups[variables['fill']]==fillval)
                    height = lookups[mask]['__calc_weight__'].sum()
                    mask = (lookups[variables['x']]==x_level) & (lookups[variables['fill']] < fillval)
                    ypos = lookups[mask]['__calc_weight__'].sum()
            else:
                if fill_levels is not None:
                    dodge = (width * fill_idx)
                else:
                    dodge = width
                ypos = 0.0
                height = row[weight_col].sum()

            xy = (dodge + i  - fill_x_adjustment, ypos)

            ax.add_patch(patches.Rectangle(xy, width, height, **params))
            if fill_levels is not None:
                xticks.append(i)
            else:
                xticks.append(i + dodge)

        # need this b/c we're using patches
        ax.autoscale_view()

        # this will happen multiple times, but it's ok b/c it'll be the same each time
        ax.set_xticks(xticks)
        ax.set_xticklabels(x_levels)

class geom_rect(geom):

    DEFAULT_AES = {'alpha': None, 'color': None, 'fill': '#333333',
                   'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'xmin', 'xmax', 'ymin', 'ymax'}
    DEFAULT_PARAMS = {}
    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth',
                    'fill': 'facecolor', 'color': 'edgecolor'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
        xmin = data[variables['xmin']]
        xmax = data[variables['xmax']]
        ymin = data[variables['ymin']]
        ymax = data[variables['ymax']]

        params = self._get_plot_args(data, _aes)

        for (xmin_i, xmax_i, ymin_i, ymax_i) in zip(xmin.values, xmax.values, ymin.values, ymax.values):
            ax.add_patch(
                    patches.Rectangle(
                        (xmin_i, ymin_i),       # (x,y)
                        xmax_i - xmin_i ,          # width
                        ymax_i - ymin_i ,          # height
                        **params
                    )
            )
        # matplotlib patches don't automatically impact the scale of the ax, so
        # we manually autoscale the x and y axes
        ax.autoscale_view()

class geom_tile(geom):

    DEFAULT_AES = {'alpha': None, 'color': None, 'fill': '#333333',
                   'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'x', 'y'}
    DEFAULT_PARAMS = {'xbins': 20, 'ybins': 20}
    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth',
                    'fill': 'facecolor', 'color': 'edgecolor'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
        x = data[variables['x']]
        y = data[variables['y']]

        weight = variables['fill']
        if 'fill' in variables:
            del variables['fill']

        params = self._get_plot_args(data, _aes)

        n_xbins = self.params.get('xbins', _calc_n_bins(x))
        n_ybins = self.params.get('ybins', _calc_n_bins(y))
        x_cut, x_bins = pd.cut(x, n_xbins, retbins=True)
        y_cut, y_bins = pd.cut(y, n_ybins, retbins=True)
        data[variables['x'] + "_cut"] = x_cut
        data[variables['y'] + "_cut"] = y_cut
        counts = data[[weight, variables['x'] + "_cut", variables['y'] + "_cut"]].groupby([variables['x'] + "_cut", variables['y'] + "_cut"]).count().fillna(0)
        weighted = data[[weight, variables['x'] + "_cut", variables['y'] + "_cut"]].groupby([variables['x'] + "_cut", variables['y'] + "_cut"]).sum().fillna(0)

        def get_xy():
            for x in x_bins:
                for y in y_bins:
                    yield (x, y)
        xy = get_xy()

        xstep = x_bins[1] - x_bins[0]
        ystep = y_bins[1] - y_bins[0]
        maxval = counts.max().max() * weighted.max().max()

        for ((idx, cnt), (_, wt)) in zip(counts.iterrows(), weighted.iterrows()):
            xi, yi = next(xy)
            params['alpha'] = (wt.values * cnt.values) / float(maxval)
            ax.add_patch(
                    patches.Rectangle(
                        (xi, yi),       # (x,y)
                        xstep,          # width
                        ystep,          # height
                        **params
                    )
            )

        # matplotlib patches don't automatically impact the scale of the ax, so
        # we manually autoscale the x and y axes
        ax.autoscale_view()

class geom_bin2d(geom_tile):
    pass

class geom_step(geom):
    DEFAULT_AES = {'color': 'black', 'alpha': 1.0, 'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'x', 'y'}
    DEFAULT_PARAMS = {'direction': 'hv'}

    _aes_renames = {'size': 'linewidth', 'linetype': 'linestyle'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
        x = data[variables['x']]
        y = data[variables['y']]

        params = self._get_plot_args(data, _aes)

        xs = [None] * (2 * (len(x)-1))
        ys = [None] * (2 * (len(x)-1))

        # create stepped path -- interleave x with
        # itself and y with itself
        if self.params.get('direction', self.DEFAULT_PARAMS['direction']) == 'hv':
            xs[::2], xs[1::2] = x[:-1], x[1:]
            ys[::2], ys[1::2] = y[:-1], y[:-1]
        elif self.params.get('direction', self.DEFAULT_PARAMS['direction']) == 'vh':
            xs[::2], xs[1::2] = x[:-1], x[:-1]
            ys[::2], ys[1::2] = y[:-1], y[1:]

        ax.plot(xs, ys, **params)

class stat_smooth(geom):

    DEFAULT_AES = {'color': 'black'}
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

        smoothed_data = pd.DataFrame(dict(x=x, y=y, y1=y1, y2=y2))
        smoothed_data = smoothed_data.sort_values('x')

        params = self._get_plot_args(data, _aes)
        if 'alpha' not in params:
            params['alpha'] = 0.2

        order = np.argsort(x)
        if self.params.get('se', True)==True:
            # TODO: fix for dates
            ax.fill_between(smoothed_data.x, smoothed_data.y1, smoothed_data.y2, **params)
        if self.params.get('fit', True)==True:
            del params['alpha']
            ax.plot(smoothed_data.x, smoothed_data.y, **params)

stat_density = geom_density
