from .geom import geom
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class geom_boxplot(geom):
    DEFAULT_AES = {'y': None, 'color': 'black', 'flier_marker': '+'}
    REQUIRED_AES = {'x', 'y'}
    DEFAULT_PARAMS = {'stat': 'identity', 'position': 'identity'}

    def plot(self, ax, data, _aes, x_levels):
        x_levels = sorted(x_levels)
        variables = _aes.data
        x = data[variables['x']]
        y = data[variables['y']]
        params = self._get_plot_args(data, _aes)

        xticks = []
        for (i, xvalue) in enumerate(x_levels):
            subset = data[data[variables['x']]==xvalue]
            xi = np.repeat(i, len(subset))
            yvalues = subset[variables['y']]
            xticks.append(i)

            bounds_25_75 = yvalues.quantile([0.25, 0.75]).values
            bounds_5_95 = yvalues.quantile([0.05, 0.95]).values

            # TODO: make sure user wants this
            mask = ((yvalues > bounds_5_95[1]) | (yvalues < bounds_5_95[0])).values
            ax.scatter(x=xi[mask], y=yvalues[mask], c='black')

            # TODO: make sure user wants this
            ax.vlines(x=i, ymin=bounds_25_75[1], ymax=bounds_5_95[1])
            ax.vlines(x=i, ymin=bounds_5_95[0], ymax=bounds_25_75[0])

            # TODO: make sure user wants this
            ax.hlines(yvalues.median(), i - 0.25, i + 0.25, linewidth=2)

            params = {
                'facecolor': 'white',
                'edgecolor': 'black',
                'linewidth': 1
            }
            # TODO: make sure user wants this
            ax.add_patch(
                patches.Rectangle(
                    (i - 0.25, bounds_25_75[0]),
                    0.5,
                    bounds_25_75[1] - bounds_25_75[0],
                    **params
                )
            )
        # q = ax.boxplot(x, vert=True)
        # plt.setp(q['boxes'], color=params['color'])
        # plt.setp(q['whiskers'], color=params['color'])
        # plt.setp(q['fliers'], color=params['color'])

        ax.autoscale_view()

        ax.set_xticks(xticks)
        ax.set_xticklabels(x_levels)
