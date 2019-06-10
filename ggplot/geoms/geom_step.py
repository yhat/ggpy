from .geom import geom

class geom_step(geom):
    """
    Same as geom_path but with step-wise interpolation between points

    Parameters
    ----------
    x:
        x values for (x, y) coordinates
    y:
        y values for (x, y) coordinates
    color:
        color of line
    alpha:
        transparency of color
    linetype:
        type of the line ('solid', 'dashed', 'dashdot', 'dotted')
    size:
        thickness of line

    Examples
    --------
    """

    DEFAULT_AES = {'color': 'black', 'alpha': 1.0, 'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'x', 'y'}
    DEFAULT_PARAMS = {'direction': 'hv'}

    _aes_renames = {'size': 'linewidth', 'linetype': 'linestyle'}

    def plot(self, ax, data, _aes):
        (data, _aes) = self._update_data(data, _aes)
        params = self._get_plot_args(data, _aes)
        variables = _aes.data
        x = data[variables['x']]
        y = data[variables['y']]

        nulls = (x.isnull() | y.isnull())
        x = x[nulls  == False]
        y = y[nulls  == False]

        xs = [None] * (2 * (len(x)-1))
        ys = [None] * (2 * (len(x)-1))

        # create stepped path -- interleave x with
        # itself and y with itself
        if self.params.get('direction', self.DEFAULT_PARAMS['direction']) == 'hv':
            xs[::2], xs[1::2] = x[:-1], x[1:]
            ys[::2], ys[1::2] = y[:-1], y[:-1]
        elif self.params.get('direction', self.DEFAULT_PARAMS['direction']) == 'vh':
            xs[::2], xs[1::2] = x[:-1], x[:-1]
            ys[::2], ys[1::2] = y[:-1], y[1:]

        ax.plot(xs, ys, **params)
