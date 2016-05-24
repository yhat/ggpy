from .geom import geom


class geom_violin(geom):
    DEFAULT_AES = {'y': None, 'color': 'black'}
    REQUIRED_AES = {'x', 'y'}
    DEFAULT_PARAMS = {'stat': 'identity', 'position': 'identity'}

    def plot(self, ax, data, _aes, x_levels):
        params = self._get_plot_args(data, _aes)
        x_levels = sorted(x_levels)
        variables = _aes.data

        xticks = []
        for (i, xvalue) in enumerate(x_levels):
            subset = data[data[variables['x']]==xvalue]
            yi = subset[variables['y']].values
            ax.violinplot(yi, positions=[i], showextrema=False)
            xticks.append(i)

        ax.set_xticks(xticks)
        ax.set_xticklabels(x_levels)
