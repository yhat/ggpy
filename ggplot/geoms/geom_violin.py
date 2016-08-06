from .geom import geom


class geom_violin(geom):
    """
    Violin plots

    Parameters
    ----------
    x:
        x values for (x, y) coordinates
    y:
        y values to be violin'd
    color:
        color of line

    Examples
    --------
    """
    DEFAULT_AES = {'y': None, 'color': 'black'}
    REQUIRED_AES = {'x', 'y'}
    DEFAULT_PARAMS = {}

    def plot(self, ax, data, _aes, x_levels):
        (data, _aes) = self._update_data(data, _aes)
        params = self._get_plot_args(data, _aes)
        variables = _aes.data

        xticks = []
        for (i, xvalue) in enumerate(x_levels):
            subset = data[data[variables['x']]==xvalue]
            yi = subset[variables['y']].values

            # so this is weird, apparently violinplot is *the only plot that
            # you can't set the color, shape, etc. as an argument. i know, it
            # makes no sense (http://stackoverflow.com/questions/26291479/changing-the-color-of-matplotlibs-violin-plots)
            plot_parts = ax.violinplot(yi, positions=[i], showextrema=False)
            for pc in plot_parts['bodies']:
                # TODO: make this pull from params
                pc.set_facecolor('white')
                pc.set_edgecolor('black')
                pc.set_alpha(1.0)
                pc.set_linewidth(1.0)

            xticks.append(i)

        ax.set_xticks(xticks)
        ax.set_xticklabels(x_levels)
