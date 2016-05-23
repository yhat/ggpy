from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap

from patsy.eval import EvalEnvironment

import numpy as np
import pandas as pd
import warnings
import itertools

from .aes import aes
from .legend import make_legend
from .themes import theme_gray
from . import discretemappers

import pprint as pp
from PIL import Image



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
        # figure out which is which between data and aesthetics
        if not isinstance(data, pd.DataFrame):
            aesthetics, data = data, aesthetics
        self._aes = aesthetics
        self.data = data.copy()
        self._evaluate_aes_expressions()
        self.data = self._aes.handle_identity_values(self.data)

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

        self.scale_identity  = set()

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
        self.facets = None

        # colors
        self.colormap = None
        self.manual_color_list = []

        # coordinate system
        self.coords = None


    def __repr__(self):
        self.make()
        # this is nice for dev but not the best for "real"
        # self.fig.savefig('/tmp/ggplot.png', dpi=160)
        # img = Image.open('/tmp/ggplot.png')
        # img.show()
        plt.show()
        return "<ggplot: (%d)>" % self.__hash__()

    def _evaluate_aes_expressions(self):
        """
        Evaluates patsy expressions within the aesthetics (i.e. 'x + 1'
        or factor(x))
        """
        for key, item in self._aes.items():
            if item not in self.data:
                def factor(s, levels=None, labels=None):
                    return s.apply(str)

                env = EvalEnvironment.capture(eval_env=(self._aes.__eval_env__ or 1)).with_outer_namespace({ "factor": factor, "pd": pd, "np": np })
                try:
                    new_val = env.eval(item, inner_namespace=self.data)
                    self.data[item] = new_val
                except:
                    pass

    def add_labels(self):
        labels = [(self.fig.suptitle, self.title)] #, (plt.xlabel, self.xlab), (plt.ylabel, self.ylab)]
        for mpl_func, label in labels:
            if label:
                mpl_func(label)

        if not self.facets:
            return
        if self.facets.is_wrap:
            return
        if self.facets.rowvar:
            for row, name in enumerate(sorted(self.data[self.facets.rowvar].unique())):
                if self.facets.is_wrap==True:
                    continue
                elif self.facets.colvar:
                    ax = self.subplots[row][-1]
                else:
                    ax = self.subplots[row]
                ax.yaxis.set_label_position("right")
                ax.yaxis.labelpad = 10
                ax.set_ylabel(name, fontsize=10, rotation=-90)

        if self.facets.colvar:
            for col, name in enumerate(sorted(self.data[self.facets.colvar].unique())):
                if len(self.subplots.shape) > 1:
                    col = col % self.facets.ncol
                    ax = self.subplots[0][col]
                else:
                    ax = self.subplots[col]
                ax.set_title(name, fontdict={'fontsize': 10})

    def apply_limits(self):
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
        """
        'Flat' iterator for subplots. Let's you do a for-loop over each subplot
        which can be very handy.
        """
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

    def add_legend(self, legend):
        if legend:
            plt.subplots_adjust(right=0.825)
        if self.facets:
            if len(self.subplots.shape) > 1:
                i, j = self.subplots.shape
                i, j = int((i - 1) / 2), int(j - 1)
                ax = self.subplots[i][j]
                make_legend(ax, legend)
            elif self.facets.rowvar:
                i, = self.subplots.shape
                i = int((i - 1) / 2)
                ax = self.subplots[i]
                make_legend(ax, legend)
            elif self.facets.colvar:
                ax = self.subplots[-1]
                make_legend(ax, legend)
        else:
            make_legend(self.subplots, legend)

    def _get_mapping(self, aes_type, colname):
        """
        Converts a discrete aesthetic to a value that will be displayed. For example
        from "a" => "#4682B4".
        """
        mapping = None
        if aes_type=="color":
            mapping = discretemappers.color_gen(self.data[colname].nunique(), colors=self.manual_color_list)
        elif aes_type=="fill":
            mapping = discretemappers.color_gen(self.data[colname].nunique())
        elif aes_type=="shape":
            mapping = discretemappers.shape_gen()
        elif aes_type=="linetype":
            mapping = discretemappers.linetype_gen()
        elif aes_type=="size":
            mapping = discretemappers.size_gen(self.data[colname].unique())
        return mapping

    def _construct_plot_data(self):
        "Splits up the main data based on discrete aesthetics into sub-data frames"
        data = self.data
        discrete_aes = self._aes._get_discrete_aes(data)
        mappers = {}
        for aes_type, colname in discrete_aes:
            mapper = {}
            if aes_type in self.scale_identity:
                for item in sorted(data[colname].unique()):
                    mapper[item] = item
            else:
                mapping = self._get_mapping(aes_type, colname)
                if mapping is None:
                    continue

                for item in sorted(data[colname].unique()):
                    mapper[item] = next(mapping)

            mappers[aes_type] = { "name": colname, "lookup": mapper }
            data[colname + "_" + aes_type] = self.data[colname].apply(lambda x: mapper[x])
            self._aes.data[aes_type] = colname + "_" + aes_type

        discrete_aes_types = [aes_type for aes_type, _ in discrete_aes]
        # checks for continuous aesthetics that can also be discrete (color, alpha, fill, linewidth???)
        if "color" in self._aes.data and "color" not in discrete_aes_types:
            # This is approximate, going to roll with it
            if self.colormap:
                self._aes.data['colormap'] = cmap = self.colormap
            else:
                self._aes.data['colormap'] = cmap = LinearSegmentedColormap.from_list('gradient2n', ['#1f3347', '#469cef'])
            colname = self._aes.data['color']
            quantiles_actual = quantiles = data[colname].quantile([0., .2, 0.4, 0.5, 0.6, 0.75, 1.0])
            # TODO: NOT SURE IF THIS ACTUALLY WORKS WELL. could get a divide by 0 error
            quantiles = (quantiles - quantiles.min()) / (quantiles.max()) # will be bug if max is 0
            mappers['color'] = { "name": colname, "lookup": {} }
            colors = cmap(quantiles)
            for i, q in enumerate(quantiles_actual):
                mappers['color']['lookup'][q] = colors[i]
            data[colname] = (data[colname] - data[colname].min()) / data[colname].max()

        if "alpha" in self._aes.data and "alpha" not in discrete_aes_types:
            colname = self._aes.data['alpha']
            quantiles = data[colname].quantile([0., .2, 0.4, 0.5, 0.6, 0.75, 0.95])
            # TODO: NOT SURE IF THIS ACTUALLY WORKS WELL. could get a divide by 0 error
            quantiles_scaled = (quantiles - quantiles.min()) / (quantiles.max()) # will be bug if max is 0
            mappers['alpha'] = {
                "name": colname,
                "lookup": dict(zip(quantiles.values, quantiles_scaled.values))
            }
            data[colname] = (data[colname] - data[colname].min()) / data[colname].max()
            discrete_aes.append(('alpha', colname))

        if "size" in self._aes.data and "size" not in discrete_aes_types:
            colname = self._aes.data['size']
            quantiles = data[colname].quantile([0., .2, 0.4, 0.5, 0.6, 0.75, 0.95])
            # TODO: NOT SURE IF THIS ACTUALLY WORKS WELL. could get a divide by 0 error
            quantiles_scaled = (quantiles - quantiles.min()) / (quantiles.max()) # will be bug if max is 0
            mappers['size'] = {
                "name": colname,
                "lookup":  dict(zip(quantiles.values, 100 * quantiles_scaled.values))
            }
            data[colname] = 100 * (data[colname] - data[colname].min()) / data[colname].max()
            discrete_aes.append(('size', colname))

        groups = [column for _, column in discrete_aes]
        if groups:
            return mappers, data.groupby(groups)
        else:
            return mappers, [(0, data)]

    def make_facets(self):
        "Creates figure and axes for m x n facet grid/wrap"
        sharex, sharey = True, True
        if self.facets:
            if self.facets.scales=="free":
                sharex, sharey = False, False
            elif self.facets.scales=="free_x":
                sharex, sharey = False, True
            elif self.facets.scales=="free_y":
                sharex, sharey = True, False

        facet_params = dict(sharex=sharex, sharey=sharey)

        nrow, ncol = self.facets.nrow, self.facets.ncol
        facet_params['nrows'] = nrow
        facet_params['ncols'] = ncol

        if self.coords=="polar":
            facet_params['subplot_kw'] = { "polar": True }

        fig, axs = plt.subplots(**facet_params)
        return fig, axs

    def get_subplot(self, row, col):
        "Fetches subplot corresponding to row/column"
        if row is not None and col is not None:
            return self.subplots[int(row)][col]
        elif row is not None:
            return self.subplots[int(row)]
        elif col is not None:
            return self.subplots[int(col)]
        else:
            raise Exception("row and col were none!" + str(row) + ", " + str(col))

    def get_facet_groups(self, group):
        "???"
        if self.facets is None:
            yield (self.subplots, group)
            return

        col_variable = self.facets.colvar
        row_variable = self.facets.rowvar
        if self.facets.is_wrap==True:
            groups = [row_variable, col_variable]
            groups = [g for g in groups if g]
            for (i, (name, subgroup)) in enumerate(group.groupby(groups)):

                # TODO: doesn't work when these get mapped to discrete values.
                #  this only happens when a field is being used both as a facet parameter AND as a discrete aesthetic (i.e. shape)
                row, col = self.facets.facet_map[name]

                if len(self.subplots.shape)==1:
                    ax = self.subplots[i]
                else:
                    ax = self.get_subplot(row, col)

                font = { 'fontsize': 10 }
                yield (ax, subgroup)

            for item in self.facets.generate_subplot_index(self.data, self.facets.rowvar, self.facets.colvar):
                row, col = self.facets.facet_map[item]
                ax = self.get_subplot(row, col)
                if isinstance(item, tuple):
                    title = ", ".join([str(i) for i in item])
                else:
                    title = str(item)
                ax.set_title(title, fontdict=font)

            # remove axes that aren't being used
            for i in range(self.facets.ndim, self.facets.nrow * self.facets.ncol):
                row = i / self.facets.ncol
                col = i % self.facets.ncol
                ax = self.get_subplot(row, col)
                try:
                    self.fig.delaxes(ax)
                except:
                    pass

        elif col_variable and row_variable:
            for (_, (colname, subgroup)) in enumerate(group.groupby(col_variable)):
                for (_, (rowname, facetgroup)) in enumerate(subgroup.groupby(row_variable)):
                    row, col = self.facets.facet_map[(rowname, colname)]
                    ax = self.get_subplot(row, col)
                    yield (ax, facetgroup)

        elif col_variable:
            for (_, (colname, subgroup)) in enumerate(group.groupby(col_variable)):
                row, col = self.facets.facet_map[colname]
                ax = self.subplots[col]
                if self.facets.is_wrap==True:
                    ax.set_title("%s=%s" % (col_variable, colname))
                else:
                    ax.set_title(colname, fontdict={'fontsize': 10})
                yield (ax, subgroup)

        elif row_variable:
            for (row, (rowname, subgroup)) in enumerate(group.groupby(row_variable)):
                row, col = self.facets.facet_map[rowname]

                if self.facets.is_wrap==True:
                    ax = self.subplots[row]
                    ax.set_title("%s=%s" % (row_variable, rowname))
                else:
                    ax = self.subplots[row]
                    ax.yaxis.set_label_position("right")
                    ax.yaxis.labelpad = 10
                    ax.set_ylabel(rowname, fontsize=10, rotation=-90)

                yield (ax, subgroup)
        else:
            yield (self.subplots, group)

    def save(self, filename, width=None, height=None):
        """
        Save ggplot to a .png file.

        Parameters
        ----------
        filename : string
            filepath to save to
        width: int, float
            width of the plot in inches
        height: int, float
            width of the plot in inches
        """
        self.make()
        w, h = self.fig.get_size_inches()
        if width:
            w = width
        if height:
            h = height
        self.fig.set_size_inches(w, h)
        self.fig.savefig(filename)

    def make(self):
        "Constructs the plot using the methods. This is the 'main' for ggplot"
        plt.close()
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
            self._aes.legend = legend
            for _, group in groups:
                for ax, facetgroup in self.get_facet_groups(group):
                    for layer in self.layers:
                        if layer.__class__.__name__=="geom_bar":
                            mask = True
                            df = layer.setup_data(self.data, self._aes, facets=self.facets)
                            if self.facets:
                                facet_filter = facetgroup[self.facets.facet_cols].iloc[0].to_dict()
                                for k, v in facet_filter.items():
                                    mask = (mask) & (df[k]==v)
                                df = df[mask]

                            if 'fill' in self._aes:
                                fill_levels = self.data[self._aes['fill']].unique()
                            else:
                                fill_levels = None
                            layer.plot(ax, facetgroup, self._aes, x_levels=self.data[self._aes['x']].unique(),
                                fill_levels=fill_levels, lookups=df)
                        else:
                            layer.plot(ax, facetgroup, self._aes)

            self.apply_limits()
            self.add_labels()
            self.apply_axis_scales()
            self.apply_axis_labels()
            self.apply_coords()
            self.add_legend(legend)

            if self.theme:
                for ax in self._iterate_subplots():
                    self.theme.apply_final_touches(ax)
