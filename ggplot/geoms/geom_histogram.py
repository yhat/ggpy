from .geom import geom

class geom_histogram(geom):
    """
    Histogram of x data

    x:
        ...description...
    color:
        ...description...
    alpha:
        ...description...
    size:
        ...description...
    linetype:
        ...description...
    fill:
        ...description...

    Examples
    --------
    """

    DEFAULT_AES = {'alpha': None, 'color': None, 'fill': '#333333',
                   'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'x'}
    DEFAULT_PARAMS = {}
    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth',
                    'fill': 'color', 'color': 'edgecolor'}

    def plot(self, ax, data, _aes):
        params = self._get_plot_args(data, _aes)
        variables = _aes.data
        x = data[variables['x']]
        x = x[x.isnull()==False]
        ax.hist(x, **params)
