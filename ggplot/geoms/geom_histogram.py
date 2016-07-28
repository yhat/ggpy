from .geom import geom

class geom_histogram(geom):
    """
    Histogram of x data

    x:
        values to be binned and counted
    color:
        color of the outer line
    alpha:
        transparency of fill
    size:
        thickness of outer line
    linetype:
        type of the outer line ('solid', 'dashed', 'dashdot', 'dotted')
    fill:
        color the interior of the bar will be

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
        (data, _aes) = self._update_data(data, _aes)
        params = self._get_plot_args(data, _aes)
        variables = _aes.data
        x = data[variables['x']]
        x = x[x.isnull()==False]
        ax.hist(x, **params)
