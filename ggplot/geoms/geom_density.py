from scipy.stats import gaussian_kde
import numpy as np

from .geom import geom

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
