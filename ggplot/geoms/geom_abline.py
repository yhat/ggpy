from .geom import geom

class geom_abline(geom):
    """
    Line specified by slope and intercept

    slope:
        ...description...
    intercept:
        ...description...
    color:
        ...description...
    linetype:
        ...description...
    x:
        ...description...
    y:
        ...description...
    alpha:
        ...description...
    size:
        ...description...

    Examples
    --------
    """

    DEFAULT_AES = {'color': 'black', 'linetype': 'solid',
                   'alpha': None, 'size': 1.0, 'x': None,
                   'y': None}
    REQUIRED_AES = {'slope', 'intercept'}
    DEFAULT_PARAMS = {}

    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth'}

    def plot(self, ax, data, _aes):
        params = self._get_plot_args(data, _aes)
        variables = _aes.data

        slope = self.params.get('slope', 1)
        intercept = self.params.get('intercept', 0)
        _aes['slope'] = slope
        _aes['intercept'] = intercept

        x = ax.get_xticks()
        y = ax.get_xticks() * slope + intercept
        # don't need the original params from the aesthetics
        del params['x']
        del params['y']
        if 'slope' in params:
            del params['slope']
        if 'intercept' in params:
            del params['intercept']
        ax.plot(x, y, **params)
