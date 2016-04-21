import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from aes import aes
import warnings
import itertools
from matplotlib.colors import rgb2hex
from themes import theme_gray

SHAPES = [
    'o',#circle
    '^',#triangle up
    'D',#diamond
    'v',#triangle down
    '+',#plus
    'x',#x
    's',#square
    '*',#star
    'p',#pentagon
    '*'#octagon
]

def shape_gen():
    while True:
        for shape in SHAPES:
            yield shape

def palette_gen():
    generator = itertools.cycle(sns.color_palette())
    while True:
        yield rgb2hex(next(generator))

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

        # faceting
        self.grid = None
        self.facets = { }

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
        if self.facets.get("row") and self.facets.get("col"):
            middle_col = self.data[self.facets['col']].nunique() / 2
            self.subplots[middle_col].set_xlabel(xlab)
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
            ylab = self._aes.get('y')
        if self.facets.get("row") and self.facets.get("col"):
            middle_col = self.data[self.facets['col']].nunique() / 2
            self.subplots[middle_col].set_ylabel(ylab)
        elif self.facets.get("row"):
            middle_col = self.data[self.facets['row']].nunique() / 2
            self.subplots[middle_col].set_ylabel(ylab)
        elif self.facets.get("col"):
            self.subplots[0].set_ylabel(ylab)
        else:
            self.subplots.set_ylabel(ylab)


    def _construct_plot_data(self):
        data = self.data
        discrete_aes = self._aes._get_categoricals(data)
        for aes_type, colname in discrete_aes:
            mapper = {}
            if aes_type=="color":
                mapping = palette_gen()
            elif aes_type=="shape":
                mapping = shape_gen()

            for item in data[colname].unique():
                mapper[item] = next(mapping)

            data[colname] = self.data[colname].apply(lambda x: mapper[x])
        groups = [column for _, column in discrete_aes]
        if groups:
            return data.groupby(groups)
        else:
            return [(0, data)]

    def make_facets(self):
        facet_params = dict(sharex=True, sharey=True)

        facet_row = self.facets['row']
        if facet_row:
            n_row = self.data[facet_row].nunique()
            facet_params['nrows'] = n_row
        else:
            n_row = 1

        facet_col = self.facets['col']
        if facet_col:
            n_col = self.data[facet_col].nunique()
            facet_params['ncols'] = n_col
        else:
            n_col = 1

        fig, subplots = plt.subplots(**facet_params)

        if facet_row and facet_col:
            for row in range(n_row):
                for col in range(n_col):
                    subplot = subplots[row][col]
        elif facet_row:
            for row in range(n_row):
                subplot = subplots[row]
        elif facet_col:
            for col in range(n_col):
                subplot = subplots[col]

        return subplots

    def get_facet_groups(self, group):
        col_variable = self.facets.get('col')
        row_variable = self.facets.get('row')

        # there are 3 situations. faceting on rows and columns, just rows, and
        # just columns. i broke this up into 3 explicit parts b/c it can get
        # very confusing if you're trying to handle the 3 cases simultaneously. so
        # while it's possible to do it all at once, WE'RE NOT GOING TO DO THAT
        if col_variable and row_variable:
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
                self.subplots = self.make_facets()
            else:
                fig, ax = plt.subplots()
                self.subplots = ax

            self.apply_scales()

            for _, group in self._construct_plot_data():
                for ax, facetgroup in self.get_facet_groups(group):
                    for layer in self.layers:
                        layer.plot(ax, facetgroup, self._aes.data)

            self.impose_limits()
            self.add_labels()
            self.apply_axis_labels()
            plt.show()
