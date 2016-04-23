import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import numpy as np
from aes import aes
import warnings
import itertools
from matplotlib.colors import rgb2hex
from themes import theme_gray
import discretemappers


class ggplot(object):

    def __init__(self, obj1, obj2):
        self.layers = []
        if isinstance(obj1, aes):
            self._aes = obj1
            self.data = obj2
        else:
            self._aes = obj2
            self.data = obj1

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

        self.ybreaks = None
        self.ytick_labels = None

        # faceting
        self.grid = None
        self.facets = {}

        # colors
        self.colormap = None
        self.manual_color_list = []

    def add_labels(self):
        labels = [(plt.title, self.title), (plt.xlabel, self.xlab), (plt.ylabel, self.ylab)]
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

        if self.ybreaks:
            for ax in self._iterate_subplots():
                ax.yaxis.set_ticks(self.ybreaks)
        if self.ytick_labels:
            if isinstance(self.ytick_labels, list):
                for ax in self._iterate_subplots():
                    ax.yaxis.set_ticklabels(self.ytick_labels)

        # self.fig.suptitle(xlab, x=0.5, y=0.05)
        if self.facets.get("wrap")==True:
            pass
        elif self.facets.get("row") and self.facets.get("col"):
            middle_col = self.data[self.facets['col']].nunique() / 2
            self.subplots[0][middle_col].set_xlabel(xlab)
        elif self.facets.get("row"):
            self.subplots[-1].set_xlabel(xlab)
        elif self.facets.get("col"):
            middle_col = self.data[self.facets['col']].nunique() / 2
            self.subplots[middle_col].set_xlabel(xlab)
        else:
            self.subplots.set_xlabel(xlab)

        if self.ylab:
            ylab = self.ylab
        else:
            ylab = self._aes.get('y', '')


        if self.facets.get("wrap")==True:
            pass
        elif self.facets.get("row") and self.facets.get("col"):
            middle_col = self.data[self.facets['col']].nunique() / 2
            self.subplots[middle_col][0].set_ylabel(ylab)
        elif self.facets.get("row"):
            middle_col = self.data[self.facets['row']].nunique() / 2
            self.subplots[middle_col].set_ylabel(ylab)
        elif self.facets.get("col"):
            self.subplots[0].set_ylabel(ylab)
        else:
            self.subplots.set_ylabel(ylab)

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
        for aes_type, colname in discrete_aes:
            mapper = {}
            if aes_type=="color":
                mapping = discretemappers.palette_gen(self.manual_color_list)
            elif aes_type=="shape":
                mapping = discretemappers.shape_gen()
            else:
                continue

            for item in data[colname].unique():
                mapper[item] = next(mapping)


            data[colname] = self.data[colname].apply(lambda x: mapper[x])

        if self.colormap and "color" in self._aes.keys() and "color" not in discrete_aes:
            self._aes.data['colormap'] = self.colormap

        groups = [column for _, column in discrete_aes]
        if groups:
            return data.groupby(groups)
        else:
            return [(0, data)]

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
                ax = self.subplots[row][col]
                font = { 'fontsize': 10 }
                ax.set_title(', '.join(name), fontdict=font) #, backgroundcolor='#E5E5E5')
                yield (ax, subgroup)

            # remove axes that aren't being used
            for j in range(i + 1, self.facets['n_rows'] * self.facets['n_cols']):
                row = j / self.facets['n_rows']
                col = j % self.facets['n_cols']
                ax = self.subplots[row][col]
                self.fig.delaxes(ax)

        elif col_variable and row_variable:
            for (col, (colname, subgroup)) in enumerate(group.groupby(col_variable)):
                for (row, (rowname, facetgroup)) in enumerate(subgroup.groupby(row_variable)):
                    ax = self.subplots[row][col]
                    ax.set_title("%s=%s | %s=%s" % (row_variable, rowname, col_variable, colname))
                    yield (ax, facetgroup)
        elif col_variable:
            for (col, (colname, subgroup)) in enumerate(group.groupby(col_variable)):
                ax = self.subplots[col]
                ax.set_title("%s=%s" % (col_variable, colname))
                yield (ax, subgroup)
        elif row_variable:
            for (row, (rowname, subgroup)) in enumerate(group.groupby(row_variable)):
                ax = self.subplots[row]
                ax.set_title("%s=%s" % (row_variable, rowname))
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
                self.fig, self.subplots = plt.subplots()

            self.apply_scales()

            for _, group in self._construct_plot_data():
                for ax, facetgroup in self.get_facet_groups(group):
                    for layer in self.layers:
                        layer.plot(ax, facetgroup, self._aes.data)

            self.impose_limits()
            self.add_labels()
            self.apply_axis_labels()
            self.apply_axis_scales()
            if self.theme:
                for ax in self._iterate_subplots():
                    self.theme.apply_final_touches(ax)
            plt.show()
