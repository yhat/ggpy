import pandas as pd
import matplotlib.patches as patches
from .geom import geom
from ..utils import calc_n_bins

class geom_tile(geom):
    """
    Frequency table / heatmap

    Parameters
    ----------
    x:
        x values for bins/categories
    y:
        y values for bins/categories
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

    Examples
    --------
    """

    DEFAULT_AES = {'alpha': None, 'color': None, 'fill': '#333333',
                   'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'x', 'y'}
    DEFAULT_PARAMS = {'xbins': 20, 'ybins': 20, 'interpolate': False}
    _aes_renames = {'linetype': 'linestyle', 'size': 'linewidth',
                    'fill': 'facecolor', 'color': 'edgecolor'}

    def plot(self, ax, data, _aes):
        (data, _aes) = self._update_data(data, _aes)
        params = self._get_plot_args(data, _aes)
        variables = _aes.data
        x = data[variables['x']]
        y = data[variables['y']]

        weight = variables['fill']
        if 'fill' in variables:
            del variables['fill']

        n_xbins = self.params.get('xbins', calc_n_bins(x))
        n_ybins = self.params.get('ybins', calc_n_bins(y))
        x_cut, x_bins = pd.cut(x, n_xbins, retbins=True)
        y_cut, y_bins = pd.cut(y, n_ybins, retbins=True)
        data[variables['x'] + "_cut"] = x_cut
        data[variables['y'] + "_cut"] = y_cut
        counts = data[[weight, variables['x'] + "_cut", variables['y'] + "_cut"]].groupby([variables['x'] + "_cut", variables['y'] + "_cut"]).count().fillna(0)
        weighted = data[[weight, variables['x'] + "_cut", variables['y'] + "_cut"]].groupby([variables['x'] + "_cut", variables['y'] + "_cut"]).sum().fillna(0)

        if self.params['interpolate']==False:
            def get_xy():
                for x in x_bins:
                    for y in y_bins:
                        yield (x, y)
            xy = get_xy()

            xstep = x_bins[1] - x_bins[0]
            ystep = y_bins[1] - y_bins[0]
            maxval = counts.max().max() * weighted.max().max()

            for ((idx, cnt), (_, wt)) in zip(counts.iterrows(), weighted.iterrows()):
                xi, yi = next(xy)
                params['alpha'] = (wt.values * cnt.values) / float(maxval)
                ax.add_patch(
                        patches.Rectangle(
                            (xi, yi),       # (x,y)
                            xstep,          # width
                            ystep,          # height
                            **params
                        )
                )
        else:
            import matplotlib.pyplot as plt
            z = []
            for xi in x:
                z.append([xi * yi for yi in y])

            ax.contourf(x, y, z, 10, cmap=plt.cm.Blues)

        # matplotlib patches don't automatically impact the scale of the ax, so
        # we manually autoscale the x and y axes
        ax.autoscale_view()
