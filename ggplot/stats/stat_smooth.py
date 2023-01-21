import pandas as pd
import numpy as np

from ..geoms.geom import geom
from . import smoothers
from ..utils import is_date

class stat_smooth(geom):
    """
    Smoothed line charts for inspecting trends in your data. There are 3 types of
    smoothing algorithms you can use:

        LOESS ('loess', 'lowess'): Non-parmetric, local regression technique for
            calculating a smoothed curve.

        linear model ('lm'): Fits a linear model to your (x, y) coordinates

        moving average ('ma'): Calculates average of last N points in (x, y) coordinates

    In addition to plotting the smoothed line, stat_smooth will also display the
    standard error bands of the smoothed data (controlled by se=True/False).

    Parameters
    ----------
    x:
        x values for (x, y) coordinates
    y:
        y values for (x, y) coordinates. these will ultimately be smoothed
    color:
        color of the outer line
    alpha:
        transparency of color
    size:
        thickness of line
    linetype:
        type of the line ('solid', 'dashed', 'dashdot', 'dotted')
    se:
        boolean value for whether or not to display standard error bands; defaults to True
    method:
        type of smoothing to ues ('loess', 'ma', 'lm')
    window:
        number of periods to include in moving average calculation

    Examples
    --------
    """

    DEFAULT_AES = {'color': 'black'}
    DEFAULT_PARAMS = {'geom': 'smooth', 'position': 'identity', 'method': 'auto',
            'se': True, 'n': 80, 'fullrange': False, 'level': 0.95,
            'span': 2/3., 'window': None}
    REQUIRED_AES = {'x', 'y'}
    _aes_renames = {'size': 'linewidth', 'linetype': 'linestyle'}

    def plot(self, ax, data, _aes):
        (data, _aes) = self._update_data(data, _aes)
        variables = _aes.data
        x = data[variables['x']]
        y = data[variables['y']]

        params = {'alpha': 0.2}

        se = self.params.get('se', True)
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
        smoothed_data = smoothed_data.sort('x')

        params = self._get_plot_args(data, _aes)
        if 'alpha' not in params:
            params['alpha'] = 0.2

        order = np.argsort(x)
        if self.params.get('se', True)==True:
            if is_date(smoothed_data.x.iloc[0]):
                dtype = smoothed_data.x.iloc[0].__class__
                x = np.array([i.toordinal() for i in smoothed_data.x])
                ax.fill_between(x, smoothed_data.y1, smoothed_data.y2, **params)
                new_ticks = [dtype(i) for i in ax.get_xticks()]
                ax.set_xticklabels(new_ticks)
            else:
                ax.fill_between(smoothed_data.x, smoothed_data.y1, smoothed_data.y2, **params)
        if self.params.get('fit', True)==True:
            del params['alpha']
            ax.plot(smoothed_data.x, smoothed_data.y, **params)
