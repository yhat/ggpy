from .geom import geom
from ..utils import is_date
import numpy as np

class geom_ribbon(geom):
    """
    Ribbons and/or area plots

    Parameters
    ----------
    x:
        x values for (x, y) coordinates
    ymin:
        y values for bottom of ribbon
    ymax:
        y values for top of ribbon
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

    DEFAULT_AES = {'alpha': None, 'color': None, 'fill': '#333333',
                   'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'x', 'ymax', 'ymin'}
    DEFAULT_PARAMS = {}

    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth', 'fill': 'facecolor', 'color': 'edgecolor'}
    def plot(self, ax, data, _aes):
        (data, _aes) = self._update_data(data, _aes)
        params = self._get_plot_args(data, _aes)
        variables = _aes.data
        x = data[variables['x']]
        ymin = data[variables['ymin']]
        ymax = data[variables['ymax']]

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
