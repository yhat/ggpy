from .geom import geom
from ..utils import is_date
import numpy as np
import pandas as pd

class geom_area(geom):
    """
    Special case of geom_ribbon where ymin = 0

    Parameters
    ----------
    x:
        x values for (x, y) coordinates
    y:
        y values for (x, y) coordinates
    color:
        color of the outer line
    alpha:
        transparency of color
    size:
        thickness of line
    linetype:
        type of the line ('solid', 'dashed', 'dashdot', 'dotted')
    fill:
        color of the inside of the shape

    Examples
    --------
    """
    last_y = None

    DEFAULT_AES = {'alpha': None, 'color': None, 'fill': '#333333',
                   'linetype': 'solid', 'size': 0}
    REQUIRED_AES = {'x', 'y'}
    DEFAULT_PARAMS = {'position': 'stack'}

    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth', 'fill': 'facecolor', 'color': 'edgecolor'}
    def plot(self, ax, data, _aes):
        (data, _aes) = self._update_data(data, _aes)
        params = self._get_plot_args(data, _aes)
        variables = _aes.data
        x = data[variables['x']]
        if self.last_y is None:
            self.last_y = pd.Series(np.repeat(0, len(data)))
        ymin = self.last_y
        if self.DEFAULT_PARAMS['position']=="stack":
            ymax = self.last_y.reset_index(drop=True) + data[variables['y']].reset_index(drop=True)
        else:
            ymax = data[variables['y']]

        # TODO: for some reason the reordering produces NaNs
        order = x.argsort()

        # x value in fill_between can't be a date
        if is_date(x.iloc[0]):
            dtype = x.iloc[0].__class__
            x = np.array([i.toordinal() for i in x])
            ax.fill_between(x, ymin, ymax, **params)
            new_ticks = [dtype(i) for i in ax.get_xticks()]
            ax.set_xticklabels(new_ticks)
        else:
            ax.fill_between(x, ymin, ymax, **params)

        self.last_y = data[variables['y']]
