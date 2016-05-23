from .geom import geom

class geom_histogram(geom):

    DEFAULT_AES = {'alpha': None, 'color': None, 'fill': '#333333',
                   'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'x'}
    DEFAULT_PARAMS = {'stat': 'bin', 'position': 'stack'}
    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth',
                    'fill': 'color', 'color': 'edgecolor'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
        x = data[variables['x']]
        params = self._get_plot_args(data, _aes)
        ax.hist(x, **params)
