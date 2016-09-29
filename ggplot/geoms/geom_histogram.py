from .geom import geom
import numpy as np


class geom_histogram(geom):
    """
    Histogram of x data

    Parameters
    ----------
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
    binwidth:
        width of each bin in the histogram. if you specify both bins and binwidth, binwidth will be used

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
        (data, _aes) = self._update_data(data, _aes)
        params = self._get_plot_args(data, _aes)

        variables = _aes.data
        x = data[variables['x']]
        x = x[x.isnull()==False]

        if 'binwidth' in self.params:
            params['bins'] = np.arange(np.min(x), np.max(x) + self.params['binwidth'], self.params['binwidth'])
        else:
            params['bins'] = self.params['bins']
        ax.hist(x, **params)
