from .geom import geom
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pandas import Series
#from ..aes import aes
from ..ggplot import ggplot
#from matplotlib.pyplot import boxplot
from matplotlib.patches import Polygon, PathPatch, Path
from matplotlib.colors import ColorConverter

def stat_boxplot(ydata, coef = 1.5, notch=False, whiskers="Tukey"):
    """compute statistics for box plot
    Arguments:
        ydata:
            data values
        coef = 1.5:
            interquartile distance for placing whiskers and defining the outliers
        whiskers:
            one of the following options
            - "Tukey"      -- tukey style whiskers (coef argument applies)
            - float or int -- percentile (>1.0 or int) or quantile (<1.0)
            - "Spear"      -- use min and max value for whiskers
        notch = False:
            compute notch position

   Note: weighted samples are not supported currently
   """
    ydata = ydata[~np.isnan(ydata)]
    qs = [0, 0.25, 0.5, 0.75, 1]
    if whiskers is int or (whiskers is float and whiskers>1.0):
        qs[0] = 0.01*whiskers
        qs[-1] = 1-0.01*whiskers
    elif whiskers is float:
        qs[0] = whiskers
        qs[-1] = whiskers

    box_params = ydata.quantile(qs)
    box_params.index =  ("whisker_min", "lower", "median", "upper", "whisker_max")
    box_params["mean"] = ydata.mean()

    iqr  = box_params["upper"] - box_params["lower"]
    if str(whiskers).lower()=="tukey":
        _ol_margin_delta = coef * iqr
        outlier_mask = ((ydata < (box_params["lower"] - _ol_margin_delta)) |
                        ( ydata > (box_params["upper"]  + _ol_margin_delta))
                       )
    else:
        outlier_mask = ((ydata < box_params["whisker_min"]) |
                        ( ydata > box_params["whisker_max"])
                       )
    if str(whiskers).lower()=="tukey" and any(outlier_mask):
        box_params["whisker_min"] = min(box_params["lower"], min(ydata[~outlier_mask]))
        box_params["whisker_max"] = max(box_params["upper"], max(ydata[~outlier_mask]))
    #df <- as.data.frame(as.list(stats))
    #df$outliers <- list(data$y[outliers])
    #
    #if (is.null(data$weight)) {
    #  n <- sum(!is.na(data$y))
    n = (~ydata.isnull()).sum()
    #} else {
    #  # Sum up weights for non-NA positions of y and weight
    #  n <- sum(data$weight[!is.na(data$y) & !is.na(data$weight)])
    #}
    #
    if notch:
        notch_delta = 1.58 * iqr / np.sqrt(n)
        box_params["notch_upper"] = box_params["median"] + notch_delta
        box_params["notch_lower"] = box_params["median"] - notch_delta

    #if (length(unique(data$x)) > 1)
    #  width <- diff(range(data$x)) * 0.9
    #
    #df$x <- if (is.factor(data$x)) data$x[1] else mean(range(data$x))
    #df$width <- width
    box_params["relvarwidth"] = np.sqrt(n)

    outliers = ydata[outlier_mask].tolist()
    return box_params, outliers

def _median_line_(x, width, boxplot_stats, ax, **linekwargs):
    if "lw" in linekwargs:
        linekwargs["linekwargs"] = linekwargs.pop("lw")
    if "linewidth" in linekwargs:
        linekwargs = linekwargs.copy()
        linekwargs["linewidth"] = 2*linekwargs["linewidth"]
    else:
        linekwargs["linewidth"] = 2.0
    ax.hlines(boxplot_stats["median"], x - width/2.0, x + width/2.0, **linekwargs)
    return ax


def _notched_box_(x, width, boxplot_stats,
                ax=None, notchwidth=0.5, median=True, linekwargs={"linewidth":1.0}, **kwargs):
    if ax is None:
        ax=plt.gca()

    left = x - 0.5*width
    right = x + 0.5*width

    narrow_left = x - 0.5*notchwidth*width
    narrow_right = x + 0.5*notchwidth*width

    lower_quartile = boxplot_stats["lower"]
    median_ = boxplot_stats["median"]
    upper_quartile = boxplot_stats["upper"]

    if "notch_lower" in boxplot_stats:
        median_width = notchwidth*width
        notch_lower = boxplot_stats["notch_lower"]
        notch_upper = boxplot_stats["notch_upper"]

        xy = np.asarray([[left, lower_quartile],
                         [left, notch_lower],
                         [narrow_left, median_],
                         [left, notch_upper],
                         [left, upper_quartile],
                         [right, upper_quartile],
                         [right, notch_upper],
                         [narrow_right, median_],
                         [right, notch_lower],
                         [right, lower_quartile],
                         [left, lower_quartile]])
    else:
        median_width = width
        xy = np.asarray([[left, lower_quartile],
                         [left, upper_quartile],
                         [right, upper_quartile],
                         [right, lower_quartile],
                         [left, lower_quartile]])

    polygon = PathPatch(Path(xy), **kwargs)
    ax.add_patch(polygon)
    _median_line_(x, median_width, boxplot_stats, ax=ax, **linekwargs)
    ax.autoscale_view()
    return ax

def _whiskers_(x, width, boxplot_stats, ax=None, whiskerbar=False, **linekwargs):
    if ax is None:
        ax=plt.gca()
    ax.vlines(x, ymin=boxplot_stats["upper"], ymax=boxplot_stats["whisker_max"], **linekwargs)
    ax.vlines(x, ymin=boxplot_stats["whisker_min"], ymax=boxplot_stats["lower"], **linekwargs)
    if whiskerbar:
        ax.hlines(boxplot_stats["whisker_min"], x-width/4.0, x+width/4.0, **linekwargs)
        ax.hlines(boxplot_stats["whisker_max"], x-width/4.0, x+width/4.0, **linekwargs)
    return ax


def _boxplot_(yvalues, x=0, fill='w', edgecolor='k',
              outlier_color="k", lw=1.0, width=0.5, ax=None,
              quantiles=False, percentiles=False,
              whiskerbar=False,
              box=True,
              notch=False,
              notchwidth = 0.5,
              outliers = True,
              outlier_marker = ".",
              alpha=1.0,
              whiskers="Tukey"):
    if ax is None:
        ax = plt.gca()

    # get parameters for line plotting
    linekwargs=dict(color=edgecolor, linewidth=lw)
    # compute stats
    boxplot_stats, outlier_list = stat_boxplot(yvalues, notch=notch,
                                               whiskers=whiskers,)
    #plot the box
    if box:
        _notched_box_(x, width, boxplot_stats, ax=ax,
                      notchwidth=notchwidth,
                      facecolor=fill,
                      alpha=alpha,
                      edgecolor=edgecolor,
                      linewidth=lw,
                      linekwargs=linekwargs)
    else:
        ax.vlines(x, ymin=boxplot_stats["lower"], ymax=boxplot_stats["upper"])
    #plot the whiskers
    ax = _whiskers_(x, width, boxplot_stats, whiskerbar=whiskerbar, ax=ax, **linekwargs)
    #plot the outliers
    if outliers:
        ax.scatter([x]*len(outlier_list), outlier_list, color=outlier_color, marker=outlier_marker)
    return ax, boxplot_stats


def _get_shade_(edgecolor, main_color, default="black"):
    "interpret a float-valued `color` as a darker(+) / lighter(-) shade of `fill`"
    if (type(edgecolor) is float):
        if abs(edgecolor) <= 1.0:
            if len(main_color)==3:
                t = 1.0 if edgecolor<0 else 0.0
                p = edgecolor if edgecolor>0 else -edgecolor
                try:
                    main_color = ColorConverter().to_rgb(main_color)
                    edgecolor = [(t-c)*p + c for c in main_color]
                except:
                    edgecolor = default
    # if whatever fails above:
    if (type(edgecolor) is float) or edgecolor is None:
            edgecolor = ColorConverter().to_rgb(default)
    return edgecolor


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
        color of line: standard matplotlib color values or a float within (0.0,1.0) to get darker shades of `fill` parameter for line color
   outlier_color:
       color of outlier markers (same value types as `color`)
    width:
        width of the box (or group of boxes if fill column is supplied)
    spacing:
        shrink box width (useful for groups when fill column is supplied)
    outlier_marker:
        type of marker used ('o', '^', 'D', 'v', 's', '*', 'p', '8', "_", "|", "_")
    notch:
        draw notches for median +/- 1.58 * IQR / sqrt(N), which gives roughly 95% confidence interval for medians; see McGill et al. (1978) for more details.
    whiskers:
        ("Tukey", "Spear", float < 1.0 for quantiles or int for percentiles)
    whiskerbar:
        bool; draw whisker bars for 5% and 95% (default: False)
    outliers:
        bool; draw outliers (default = True)
    percentiles:
        column name (default=None); if supplied, column `y` is treated as percentiles corresponding to the percentile levels set in this column
    quantiles:
        see percentiles argument

    Examples
    --------
    """
    DEFAULT_AES = {'y': None,
                   'color': 'black',
                   'outlier_color': None,
                   'outlier_marker': '+',
                   'width':0.5,
                   "notchwidth": 0.5,
                   'median':True,
                   'spacing':0.01,
                   'fill': 'white',
                   'percentiles':None,
                   'quantiles':None,
                   'notch':False,
                   'lines':True,
                   'whiskers': 'Tukey',
                   'whiskerbar':False,
                   'alpha': None,
                   'keep_stats': False,
                   'outliers':True}
    REQUIRED_AES = {'x', 'y'}
    DEFAULT_PARAMS = {}

    def __radd__(self, gg):
        if isinstance(gg, ggplot):
            gg.layers += self.layers
            if self.geom_aes is not None:
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
        # interpret a float-valued `color` as a darker(+) / lighter(-) shade of `fill`
        edgecolor = _get_shade_(params['color'], params['fill'], default=self.DEFAULT_AES["color"])
        outlier_color = _get_shade_(params['outlier_color'], params['fill'], default=edgecolor)

        # get other plotting parameters
        plotting_kwarg_keys = ["notch", "notchwidth", "whiskers", "whiskerbar",
                               "outliers", "outlier_marker", "alpha"]
        plotting_kwarg = {}
        for pk in plotting_kwarg_keys:
            if pk in params:
                plotting_kwarg[pk] = params[pk]

        # compute width adjusted for number of `fill` values
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

            _, stats_ = _boxplot_(yvalues, xtick_fill,
                      width=(width - halfspacing),
                      fill=params['fill'],
                      edgecolor=edgecolor,
                      outlier_color=outlier_color,
                      #percentiles=params.get('percentiles', False),
                      #quantiles=params.get('quantiles', False),
                      ax=ax,
                      **plotting_kwarg)

        # q = ax.boxplot(x, vert=True)
        # plt.setp(q['boxes'], color=params['color'])
        # plt.setp(q['whiskers'], color=params['color'])
        # plt.setp(q['fliers'], color=params['color'])

        ax.autoscale_view()

        ax.set_xticks(xticks)
        ax.set_xticklabels(x_levels)
