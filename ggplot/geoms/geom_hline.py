from .geom import geom
from ..utils import is_iterable

class geom_hline(geom):
    """
    Horizontal line(s)

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
    DEFAULT_AES = {'color': 'black', 'linetype': 'solid',
                   'size': 1.0,}
    REQUIRED_AES = {}
    DEFAULT_PARAMS = {}

    _aes_renames = {'size': 'linewidth', 'linetype': 'linestyle'}

    def plot(self, ax, data, _aes):
        (data, _aes) = self._update_data(data, _aes)
        params = self._get_plot_args(data, _aes)
        variables = _aes.data
        y = self.params.get('y')
        if is_iterable(y):
            for yi in y:
                ax.axhline(yi, **params)
        else:
            ax.axhline(y, **params)
