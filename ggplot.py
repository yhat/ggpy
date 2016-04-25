import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import numpy as np
import pandas as pd
from aes import aes
import warnings
import itertools
from matplotlib.colors import rgb2hex
from themes import theme_gray
import discretemappers
from legend import make_legend
import pprint as pp


class ggplot(object):
    """
    ggplot is the base layer or object that you use to define
    the components of your chart (x and y axis, shapes, colors, etc.).
    You can combine it with layers (or geoms) to make complex graphics
    with minimal effort.

    Parameters
    -----------
    aesthetics :  aes (ggplot.components.aes.aes)
        aesthetics of your plot
    data :  pandas DataFrame (pd.DataFrame)
        a DataFrame with the data you want to plot

    Examples
    ----------
    >>> p = ggplot(aes(x='x', y='y'), data=diamonds)
    >>> print(p + geom_point())
    """

    CONTINUOUS = ['x', 'y', 'size', 'alpha']
    DISCRETE = ['color', 'shape', 'marker', 'alpha', 'linestyle']

    def __init__(self, aesthetics, data):
        # ggplot should just 'figure out' which is which
        if not isinstance(data, pd.DataFrame):
            aesthetics, data = data, aesthetics
        self._aes = aesthetics
        self.data = data

        self.layers = []

        # labels
        self.title = None
        self.xlab = None
        self.ylab = None

        # limits
        self.xlimits = None
        self.ylimits = None

        # themes
        self.theme = theme_gray()

        # scales
        self.scales = []

        self.scale_x_log = None
        self.scale_y_log = None

        self.scale_x_reverse = None
        self.scale_y_reverse = None

        self.xbreaks = None
        self.xtick_labels = None
        self.xtick_formatter = None

        self.ybreaks = None
        self.ytick_labels = None
        self.ytick_formatter = None

        # faceting
        self.grid = None
        self.facets = {}

        # colors
        self.colormap = None
        self.manual_color_list = []

        # coordinate system
        self.coords = None

    def add_labels(self):
        labels = [(self.fig.suptitle, self.title)] #, (plt.xlabel, self.xlab), (plt.ylabel, self.ylab)]
        for mpl_func, label in labels:
            if label:
                mpl_func(label)

    def impose_limits(self):
        limits = [(plt.xlim, self.xlimits), (plt.ylim, self.ylimits)]
        for mpl_func, limit in limits:
            if limit:
                mpl_func(limit)

    def apply_scales(self):
        for scale in self.scales:
            scale.apply()

    def apply_theme(self):
        if self.theme:
            rcParams = self.theme.get_rcParams()
            for key, val in rcParams.items():
                # there is a bug in matplotlib which does not allow None directly
                # https://github.com/matplotlib/matplotlib/issues/2543
                try:
                    if key == 'text.dvipnghack' and val is None:
                        val = "none"
                    mpl.rcParams[key] = val
                except Exception as e:
                    msg = """Setting "mpl.rcParams['%s']=%s" raised an Exception: %s""" % (key, str(val), str(e))
                    warnings.warn(msg, RuntimeWarning)

    def apply_coords(self):
        if self.coords=="equal":
            for ax in self._iterate_subplots():
                min_val = np.min([np.min(ax.get_yticks()), np.min(ax.get_xticks())])
                max_val = np.max([np.max(ax.get_yticks()), np.max(ax.get_xticks())])
                ax.set_xticks(np.linspace(min_val, max_val, 7))
                ax.set_yticks(np.linspace(min_val, max_val, 7))
        elif self.coords=="flip":
            if 'x' in self._aes.data and 'y' in self._aes.data:
                x = self._aes.data['x']
                y = self._aes.data['y']
                self._aes.data['x'] = y
                self._aes.data['y'] = x

    def apply_axis_labels(self):
        if self.xlab:
            xlab = self.xlab
        else:
            xlab = self._aes.get('x')

        if self.xbreaks:
            for ax in self._iterate_subplots():
                ax.xaxis.set_ticks(self.xbreaks)
        if self.xtick_labels:
            if isinstance(self.xtick_labels, list):
                for ax in self._iterate_subplots():
                    ax.xaxis.set_ticklabels(self.xtick_labels)
        if self.xtick_formatter:
            for ax in self._iterate_subplots():
                labels = [self.xtick_formatter(label) for label in ax.get_xticks()]
                ax.xaxis.set_ticklabels(labels)

        if self.ybreaks:
            for ax in self._iterate_subplots():
                ax.yaxis.set_ticks(self.ybreaks)
        if self.ytick_labels:
            if isinstance(self.ytick_labels, list):
                for ax in self._iterate_subplots():
                    ax.yaxis.set_ticklabels(self.ytick_labels)

        if self.ytick_formatter:
            for ax in self._iterate_subplots():
                labels = [self.ytick_formatter(label) for label in ax.get_yticks()]
                ax.yaxis.set_ticklabels(labels)

        self.fig.text(0.5, 0.05, xlab)

        if self.ylab:
            ylab = self.ylab
        else:
            ylab = self._aes.get('y', '')

        self.fig.text(0.05, 0.5, ylab, rotation='vertical')

    def _iterate_subplots(self):
        try:
            return self.subplots.flat
        except Exception as e:
            return [self.subplots]

    def apply_axis_scales(self):
        if self.scale_x_log:
            for ax in self._iterate_subplots():
                ax.set_xscale('log', basex=self.scale_x_log)

        if self.scale_y_log:
            for ax in self._iterate_subplots():
                ax.set_yscale('log', basey=self.scale_y_log)

        if self.scale_x_reverse:
            for ax in self._iterate_subplots():
                ax.invert_xaxis()

        if self.scale_y_reverse:
            for ax in self._iterate_subplots():
                ax.invert_yaxis()

    def _construct_plot_data(self):
        data = self.data
        discrete_aes = self._aes._get_categoricals(data)
        mappers = {}
        for aes_type, colname in discrete_aes:
            mapper = {}
            if aes_type=="color":
                mapping = discretemappers.palette_gen(self.manual_color_list)
            elif aes_type=="shape":
                mapping = discretemappers.shape_gen()
            elif aes_type=="linetype":
                mapping = discretemappers.linetype_gen()
            else:
                continue

            for item in data[colname].unique():
                mapper[item] = next(mapping)
            mappers[aes_type] = mapper

            data[colname] = self.data[colname].apply(lambda x: mapper[x])

        if self.colormap and "color" in self._aes.keys() and "color" not in discrete_aes:
            self._aes.data['colormap'] = self.colormap

        groups = [column for _, column in discrete_aes]
        if groups:
            return mappers, data.groupby(groups)
        else:
            return mappers, [(0, data)]

    def make_facets(self):
        facet_params = dict(sharex=True, sharey=True)

        facet_row = self.facets['row']
        if self.facets.get('n_rows'):
            n_row = self.facets['n_rows']
            facet_params['nrows'] = n_row
        elif facet_row:
            n_row = self.data[facet_row].nunique()
            facet_params['nrows'] = n_row
        else:
            n_row = 1

        facet_col = self.facets['col']

        if self.facets.get('n_cols'):
            n_col = self.facets['n_cols']
            facet_params['ncols'] = n_col
        elif facet_col:
            n_col = self.data[facet_col].nunique()
            facet_params['ncols'] = n_col
        else:
            n_col = 1


        if self.coords=="polar":
            facet_params['subplot_kw'] = { "polar": True }

        return plt.subplots(**facet_params)

    def get_facet_groups(self, group):
        col_variable = self.facets.get('col')
        row_variable = self.facets.get('row')

        # there are 3 situations. faceting on rows and columns, just rows, and
        # just columns. i broke this up into 3 explicit parts b/c it can get
        # very confusing if you're trying to handle the 3 cases simultaneously. so
        # while it's possible to do it all at once, WE'RE NOT GOING TO DO THAT

        # TODO: this breaks when controlling the number of rows/columns in a facet grid
        if self.facets.get('wrap', False)==True:
            groups = [col_variable, row_variable]
            groups = [g for g in groups if g]
            for (i, (name, subgroup)) in enumerate(group.groupby(groups)):
                if isinstance(name, str):
                    name = [name]
                row = i / self.facets['n_rows']
                col = i % self.facets['n_cols']

                if len(self.subplots.shape)==1:
                    ax = self.subplots[i]
                else:
                    ax = self.subplots[row][col]

                font = { 'fontsize': 10 }
                ax.set_title(', '.join(name), fontdict=font) #, backgroundcolor='#E5E5E5')
                yield (ax, subgroup)

            # remove axes that aren't being used. this will only happen if we have
            # multiple fields we're wrapping ???
            for j in range(i + 1, self.facets['n_rows'] * self.facets['n_cols']):
                row = j / self.facets['n_rows']
                col = j % self.facets['n_cols']
                ax = self.subplots[row][col]
                self.fig.delaxes(ax)

        elif col_variable and row_variable:
            for (col, (colname, subgroup)) in enumerate(group.groupby(col_variable)):
                for (row, (rowname, facetgroup)) in enumerate(subgroup.groupby(row_variable)):
                    ax = self.subplots[row][col]

                    # setup labels for facet grids. this happens only for the top row
                    #  and the right-most column
                    if row==0:
                        ax.set_title(colname, fontdict={'fontsize': 10})

                    if col==0:
                        self.subplots[row][-1].yaxis.set_label_position("right")
                        self.subplots[row][-1].yaxis.labelpad = 10
                        self.subplots[row][-1].set_ylabel(rowname, fontsize=10, rotation=-90)

                    yield (ax, facetgroup)

        elif col_variable:
            for (col, (colname, subgroup)) in enumerate(group.groupby(col_variable)):
                ax = self.subplots[col]
                if self.facets['wrap']==True:
                    ax.set_title("%s=%s" % (col_variable, colname))
                else:
                    ax.set_title(colname, fontdict={'fontsize': 10})
                yield (ax, subgroup)
        elif row_variable:
            for (row, (rowname, subgroup)) in enumerate(group.groupby(row_variable)):
                ax = self.subplots[row]

                if self.facets['wrap']==True:
                    ax.set_title("%s=%s" % (row_variable, rowname))
                else:
                    ax.yaxis.set_label_position("right")
                    ax.yaxis.labelpad = 10
                    ax.set_ylabel(rowname, fontsize=10, rotation=-90)

                yield (ax, subgroup)
        else:
            yield (self.subplots, group)

    def make(self):
        # sns.set()
        with mpl.rc_context():
            self.apply_theme()

            if self.facets:
                self.fig, self.subplots = self.make_facets()
            else:
                subplot_kw = {}
                if self.coords=="polar":
                    subplot_kw = { "polar": True }
                self.fig, self.subplots = plt.subplots(subplot_kw=subplot_kw)

            self.apply_scales()

            legend, groups = self._construct_plot_data()
            for _, group in groups:
                for ax, facetgroup in self.get_facet_groups(group):
                    for layer in self.layers:
                        layer.plot(ax, facetgroup, self._aes.data)

            self.impose_limits()
            self.add_labels()
            self.apply_axis_scales()
            self.apply_axis_labels()
            self.apply_coords()

            make_legend(ax, legend)

            if self.theme:
                for ax in self._iterate_subplots():
                    self.theme.apply_final_touches(ax)

            plt.show()
