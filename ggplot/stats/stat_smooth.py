import pandas as pd
import numpy as np

from ..geoms.geom import geom
from . import smoothers
from ..utils import is_date

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

        # TODO: bug here!!!
        # 'DataFrame' object has no attribute 'sort_values'
        smoothed_data = pd.DataFrame(dict(x=x, y=y, y1=y1, y2=y2))s
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
