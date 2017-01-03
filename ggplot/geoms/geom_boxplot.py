from .geom import geom
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pandas import Series
#from ..aes import aes
from ..ggplot import ggplot

def _boxplot_(yvalues, i, params_, num_fill_levels=1,
              fill='white', edgecolor='black', outlier_color='black', lw=1.0,
              width=0.5, ax=plt.gca(),
              quantiles=False, percentiles=False):
    xi = np.repeat(i, len(yvalues))

    if not( (percentiles is None) or (percentiles is False)):
        quantiles=percentiles/100.0

    if (quantiles is None) or (quantiles is False):
        qxlist = np.r_[5, 25, 50, 75, 95] / 100.0
        qylist = yvalues.quantile(qxlist)
        if params_.get('outliers', True)==True:
            mask = ((yvalues > qylist[0.95]) | (yvalues < qylist[0.05])).values
            ax.scatter(x=xi[mask], y=yvalues[mask], c=outlier_color)
    else:
        yvalues = yvalues.groupby(quantiles).first()
        assert 0.25 in yvalues.keys()
        assert 0.5 in yvalues.keys()
        assert 0.75 in yvalues.keys()
        if params_.get('lines', True):
            assert 0.05 in yvalues.keys()
            assert 0.95 in yvalues.keys()
        qylist = yvalues

    linekwargs = dict(linewidth=lw, color=edgecolor)
    med_linekwargs = dict(linewidth=lw*2.0, color=edgecolor)

    if params_.get('lines', True)==True:
        ax.vlines(x=i, ymin=qylist[0.75], ymax=qylist[0.95], **linekwargs)
        ax.vlines(x=i, ymin=qylist[0.05], ymax=qylist[0.25], **linekwargs)

    if params_.get('notch', False)==True:
        ax.hlines(qylist[0.05], i - width/4.0, i + width/4.0, **linekwargs)
        ax.hlines(qylist[0.95], i - width/4.0, i + width/4.0, **linekwargs)

    if params_.get('median', True)==True:
        ax.hlines(qylist[0.5], i - width/2.0, i + width/2.0, **med_linekwargs)

    if params_.get('box', True)==True:
        params = {
            'facecolor': fill,
            'edgecolor': edgecolor,
            'linewidth': lw
        }
        ax.add_patch(
            patches.Rectangle(
                (i - width/2.0, qylist[0.25]),
                width,
                qylist[0.75] - qylist[0.25],
                **params
            )
        )
    else:
        ax.vlines(x=i, ymin=qylist[0.25], ymax=qylist[0.75])
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
    fill:
        a value (length 3 tuples, matplotlib literals) or column to be highlighted in fill
    color:
        color of line: standard matplotlib color values or a float within (0.0,1.0) to get darker shades of `fill` parameters for line color
   outlier_color:
       color of outlier markers (same value types as `color`)
    width:
        width of the box (or group of boxes if fill column is supplied)
    spacing:
        shrink box width (useful for groups when fill column is supplied)
    flier_marker:
        type of marker used ('o', '^', 'D', 'v', 's', '*', 'p', '8', "_", "|", "_")
    notch:
        bool; draw notch for 5% and 95% (default: False)
    outliers:
        bool; draw outliers

    Examples
    --------
    """
    DEFAULT_AES = {'y': None,
                   'color': 'black',
                   'outlier_color': 'black',
                   'flier_marker': '+',
                   'width':0.5,
                   'spacing':0.01,
                   'fill': 'white',
                   'percentiles':None,
                   'quantiles':None,
                   'notch':False,
                   'outliers':True}
    REQUIRED_AES = {'x', 'y'}
    DEFAULT_PARAMS = {}

    def __radd__(self, gg):
        if isinstance(gg, ggplot):
            gg.layers += self.layers
            for aes_key in ['fill', ]:
                if aes_key in self.geom_aes:
                    gg._aes[aes_key] = self.geom_aes.pop(aes_key)
            return gg

        self.layers.append(gg)
        return self

    def plot(self, ax, data, _aes, x_levels, fill_levels=None):
        fill_levels = fill_levels if fill_levels is not None else ['none']
        num_fill_levels = len(fill_levels)# if fill_levels is not None else 1
        (data, _aes) = self._update_data(data, _aes)
        params = self._get_plot_args(data, _aes)
        variables = _aes.data
        if 'fill' in variables:
            if variables['fill'] not in data:
                # in case when colour does not belong to any layer (is a scalar param.)
                fill_levels = [variables['fill']]
        edgecolor = params['color']
        # interpret a float-valued `color` as a darker shade of `fill`
        if (type(edgecolor) is float) and (edgecolor <= 1.0) and len(params['fill'])==3:
            edgecolor = [edgecolor*c for c in params['fill']]
        outlier_color = params.get('outlier_color', 'black')
        if (type(outlier_color) is float) and \
            (outlier_color <= 1.0) and len(params['fill'])==3:
            outlier_color = [outlier_color*c for c in params['fill']]

        width = params.get('width', 0.5)/float(num_fill_levels)
        if len(fill_levels)>1:
            halfspacing = 0.5*params.get('spacing', 0.01)
        else:
            halfspacing = 0.0
        xticks = []

        fill_layer_number = np.where(Series(fill_levels) == params['fill'])[0][0]
        for (xtick, xvalue) in enumerate(x_levels):
            xticks.append(xtick)
            mask = (data[variables['x']]==xvalue)
            yvalues = data[mask][variables['y']]
            # compute x-centre of the actual boxplot
            offset = 0.5*width*(num_fill_levels-1)
            fill_x_step = width*fill_layer_number
            xtick_fill = xtick - offset + fill_x_step

            _boxplot_(yvalues, xtick_fill, params,
                      num_fill_levels=num_fill_levels,
                      width=(width - halfspacing),
                      fill=params['fill'],
                      edgecolor=edgecolor,
                      outlier_color=outlier_color,
                      percentiles=params.get('percentiles', False),
                      quantiles=params.get('quantiles', False),
                      ax=ax)

        # q = ax.boxplot(x, vert=True)
        # plt.setp(q['boxes'], color=params['color'])
        # plt.setp(q['whiskers'], color=params['color'])
        # plt.setp(q['fliers'], color=params['color'])

        ax.autoscale_view()

        ax.set_xticks(xticks)
        ax.set_xticklabels(x_levels)
