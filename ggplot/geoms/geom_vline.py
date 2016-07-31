from .geom import geom
from ..utils import is_iterable

class geom_vline(geom):
    """
    Vertical line(s)

    Parameters
    ----------
    color:
        color of the line
    linetype:
        type of the line ('solid', 'dashed', 'dashdot', 'dotted')
    size:
        thickness of the line

    Examples
    --------
    """

    DEFAULT_AES = {'color': 'black', 'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {}
    DEFAULT_PARAMS = {}
    _aes_renames = {'size': 'linewidth', 'linetype': 'linestyle'}

    def plot(self, ax, data, _aes):
        (data, _aes) = self._update_data(data, _aes)
        params = self._get_plot_args(data, _aes)
        variables = _aes.data
        x = self.params.get('x')

        if is_iterable(x):
            for xi in x:
                ax.axvline(xi, **params)
        else:
            ax.axvline(x, **params)
