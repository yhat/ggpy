from .geom import geom
import matplotlib.patches as patches


class geom_rect(geom):

    DEFAULT_AES = {'alpha': None, 'color': None, 'fill': '#333333',
                   'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'xmin', 'xmax', 'ymin', 'ymax'}
    DEFAULT_PARAMS = {}
    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth',
                    'fill': 'facecolor', 'color': 'edgecolor'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
        xmin = data[variables['xmin']]
        xmax = data[variables['xmax']]
        ymin = data[variables['ymin']]
        ymax = data[variables['ymax']]

        params = self._get_plot_args(data, _aes)

        for (xmin_i, xmax_i, ymin_i, ymax_i) in zip(xmin.values, xmax.values, ymin.values, ymax.values):
            ax.add_patch(
                    patches.Rectangle(
                        (xmin_i, ymin_i),       # (x,y)
                        xmax_i - xmin_i ,          # width
                        ymax_i - ymin_i ,          # height
                        **params
                    )
            )
        # matplotlib patches don't automatically impact the scale of the ax, so
        # we manually autoscale the x and y axes
        ax.autoscale_view()
