from .geom import geom
from ..utils import is_iterable

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
