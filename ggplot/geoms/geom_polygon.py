from .geom import geom
import matplotlib.patches as patches


class geom_polygon(geom):

    DEFAULT_AES = {'alpha': None, 'color': None, 'fill': '#333333',
                   'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'x', 'y'}
    DEFAULT_PARAMS = {}
    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth',
                    'fill': 'facecolor', 'color': 'edgecolor'}

    def plot(self, ax, data, _aes):
        (data, _aes) = self._update_data(data, _aes)
        params = self._get_plot_args(data, _aes)
        variables = _aes.data
        x = data[variables['x']]
        y = data[variables['y']]

        coordinates = zip(x, y)
        ax.add_patch(
            patches.Polygon(
                coordinates,
                closed=True,
                fill=True,
                **params
            )
        )
        # matplotlib patches don't automatically impact the scale of the ax, so
        # we manually autoscale the x and y axes
        ax.autoscale_view()
