from .geom import geom
from ..utils import is_date

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
        if is_date(x.iloc[0]):
            dtype = x.iloc[0].__class__
            x = np.array([i.toordinal() for i in x])
            ax.fill_between(x, ymin, ymax, **params)
            new_ticks = [dtype(i) for i in ax.get_xticks()]
            ax.set_xticklabels(new_ticks)
        else:
            ax.fill_between(x, ymin, ymax, **params)
