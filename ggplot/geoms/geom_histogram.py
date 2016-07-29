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

    bins:
        number of bins in histogram

    Examples
    --------
    """

    DEFAULT_AES = {'alpha': None, 'color': None, 'fill': '#333333',
                   'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'x'}
    DEFAULT_PARAMS = {'bins': 10}
    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth',
                    'fill': 'color', 'color': 'edgecolor'}

    def plot(self, ax, data, _aes):
        params = self._get_plot_args(data, _aes)

        params['bins'] = self.params['bins']
        variables = _aes.data
        x = data[variables['x']]
        x = x[x.isnull()==False]
        ax.hist(x, **params)
