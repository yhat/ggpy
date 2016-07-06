from .geom import geom
from ..utils import is_iterable

class geom_vline(geom):

    DEFAULT_AES = {'color': 'black', 'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {}
    DEFAULT_PARAMS = {}
    _aes_renames = {'size': 'linewidth', 'linetype': 'linestyle'}

    def plot(self, ax, data, _aes):
        params = self._get_plot_args(data, _aes)
        variables = _aes.data
        x = self.params.get('x')

        if is_iterable(x):
            for xi in x:
                ax.axvline(xi, **params)
        else:
            ax.axvline(x, **params)
