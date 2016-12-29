from .geom import geom
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def _boxplot_(yvalues, i, params_, num_fill_levels=1,
              colour='white', width=0.5, ax=plt.gca()):
    xi = np.repeat(i, len(yvalues))
    bounds_25_75 = yvalues.quantile([0.25, 0.75]).values
    bounds_5_95 = yvalues.quantile([0.05, 0.95]).values

    if params_.get('outliers', True)==True:
        mask = ((yvalues > bounds_5_95[1]) | (yvalues < bounds_5_95[0])).values
        ax.scatter(x=xi[mask], y=yvalues[mask], c=params_.get('outlier_color', 'black'))

    if params_.get('lines', True)==True:
        ax.vlines(x=i, ymin=bounds_25_75[1], ymax=bounds_5_95[1])
        ax.vlines(x=i, ymin=bounds_5_95[0], ymax=bounds_25_75[0])

    if params_.get('notch', False)==True:
        ax.hlines(bounds_5_95[0], i - width/4.0, i + width/4.0, linewidth=2)
        ax.hlines(bounds_5_95[1], i - width/4.0, i + width/4.0, linewidth=2)

    if params_.get('median', True)==True:
        ax.hlines(yvalues.median(), i - width/2.0, i + width/2.0, linewidth=2)

    if params_.get('box', True)==True:
        params = {
            'facecolor': colour,
            'edgecolor': 'black',
            'linewidth': 1
        }
        ax.add_patch(
            patches.Rectangle(
                (i - width/2.0, bounds_25_75[0]),
                width,
                bounds_25_75[1] - bounds_25_75[0],
                **params
            )
        )
    else:
        ax.vlines(x=i, ymin=bounds_25_75[0], ymax=bounds_25_75[1])
    return ax

class geom_boxplot(geom):
    """
    Box and whiskers chart

    Parameters
    ----------
    x:
        x values for bins/categories
    y:
        values that will be used for box/whisker calculations
    color:
        color of line
    flier_marker:
        type of marker used ('o', '^', 'D', 'v', 's', '*', 'p', '8', "_", "|", "_")

    Examples
    --------
    """
    DEFAULT_AES = {'y': None, 'color': 'black',
                   'flier_marker': '+',
                   'width':0.5,
                   'spacing':0.01,
                   'fill': 'none'}
    REQUIRED_AES = {'x', 'y',}
    DEFAULT_PARAMS = {}

    def plot(self, ax, data, _aes, x_levels, fill_levels=None):
        fill_levels = fill_levels if fill_levels is not None else ['none']
        num_fill_levels = len(fill_levels)# if fill_levels is not None else 1
        (data, _aes) = self._update_data(data, _aes)
        params = self._get_plot_args(data, _aes)
        variables = _aes.data
        if 'fill' in variables:
            if not variables['fill'] in data:
                # create a dummy data series
                data[variables['fill']] = [variables['fill']]*data.shape[0]
                data[variables['fill']] = data[variables['fill']].astype('category')
                fill_levels = [variables['fill']]
        else:
            # create a dummy data series
            data[variables['fill']] = [fill_levels[0]]*data.shape[0]
            data[variables['fill']] = data[variables['fill']].astype('category')
        fill_data = data[variables['fill']]

        width = params.get('width', 0.5)/float(num_fill_levels)
        if len(fill_levels)>1:
            halfspacing = 0.5*params.get('spacing', 0.01)
        else:
            halfspacing = 0.0

        xticks = []
        for (xtick, xvalue) in enumerate(x_levels):
            xticks.append(xtick)
            for (fill_n, fill_value) in enumerate(fill_levels):
                mask = (data[variables['x']]==xvalue)
                mask &= (fill_data==fill_value)
                subset = data[mask]
                yvalues = subset[variables['y']]
                offset = 0.5*width*(num_fill_levels-1)
                fill_x_step = width*fill_n
                xtick_fill = xtick - offset + fill_x_step
                _boxplot_(yvalues, xtick_fill, params,
                          num_fill_levels=num_fill_levels,
                          width = width - halfspacing,
                          colour=fill_value, ax=ax)

        # q = ax.boxplot(x, vert=True)
        # plt.setp(q['boxes'], color=params['color'])
        # plt.setp(q['whiskers'], color=params['color'])
        # plt.setp(q['fliers'], color=params['color'])

        ax.autoscale_view()

        ax.set_xticks(xticks)
        ax.set_xticklabels(x_levels)
