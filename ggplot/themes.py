from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

class theme(object):
    def __init__(self):
        self._rcParams = {}

    def __radd__(self, other):
        if other.__class__.__name__=="ggplot":
            other.theme = self
            return other

        return self

    def get_rcParams(self):
        return self._rcParams

    def apply_final_touches(self, ax):
        pass


class theme_538(theme):
    """
    Theme for 538.

    Copied from CamDavidsonPilon's gist:
        https://gist.github.com/CamDavidsonPilon/5238b6499b14604367ac

   """

    def __init__(self):
        super(theme_538, self).__init__()
        self._rcParams["lines.linewidth"] = "2.0"
        # self._rcParams["examples.download"] = "True"
        self._rcParams["patch.linewidth"] = "0.5"
        self._rcParams["legend.fancybox"] = "True"
        self._rcParams["axes.prop_cycle"] = cycler('color', [ "#30a2da", "#fc4f30", "#e5ae38",
                                               "#6d904f", "#8b8b8b"])
        self._rcParams["axes.facecolor"] = "#f0f0f0"
        self._rcParams["axes.labelsize"] = "large"
        self._rcParams["axes.axisbelow"] = "True"
        self._rcParams["axes.grid"] = "True"
        self._rcParams["patch.edgecolor"] = "#f0f0f0"
        self._rcParams["axes.titlesize"] = "x-large"
        # self._rcParams["svg.embed_char_paths"] = "path"
        self._rcParams["examples.directory"] = ""
        self._rcParams["figure.facecolor"] = "#f0f0f0"
        self._rcParams["grid.linestyle"] = "-"
        self._rcParams["grid.linewidth"] = "1.0"
        self._rcParams["grid.color"] = "#cbcbcb"
        self._rcParams["axes.edgecolor"] = "#f0f0f0"
        self._rcParams["xtick.major.size"] = "0"
        self._rcParams["xtick.minor.size"] = "0"
        self._rcParams["ytick.major.size"] = "0"
        self._rcParams["ytick.minor.size"] = "0"
        self._rcParams["axes.linewidth"] = "3.0"
        self._rcParams["font.size"] ="14.0"
        self._rcParams["lines.linewidth"] = "4"
        self._rcParams["lines.solid_capstyle"] = "butt"
        self._rcParams["savefig.edgecolor"] = "#f0f0f0"
        self._rcParams["savefig.facecolor"] = "#f0f0f0"
        self._rcParams["figure.subplot.left"]   = "0.08"
        self._rcParams["figure.subplot.right"]  = "0.95"
        self._rcParams["figure.subplot.bottom"] = "0.07"

class theme_gray(theme):
    """
    Standard theme for ggplot. Gray background w/ white gridlines.

    Copied from the the ggplot2 codebase:
        https://github.com/hadley/ggplot2/blob/master/R/theme-defaults.r
    """
    def __init__(self):
        super(theme_gray, self).__init__()
        self._rcParams["timezone"] = "UTC"
        self._rcParams["lines.linewidth"] = "1.0"
        self._rcParams["lines.antialiased"] = "True"
        self._rcParams["patch.linewidth"] = "0.5"
        self._rcParams["patch.facecolor"] = "348ABD"
        self._rcParams["patch.edgecolor"] = "#E5E5E5"
        self._rcParams["patch.antialiased"] = "True"
        self._rcParams["font.family"] = "sans-serif"
        self._rcParams["font.size"] = "12.0"
        self._rcParams["font.serif"] = ["Times", "Palatino",
                                       "New Century Schoolbook",
                                       "Bookman", "Computer Modern Roman",
                                       "Times New Roman"]
        self._rcParams["font.sans-serif"] = ["Helvetica", "Avant Garde",
                                            "Computer Modern Sans serif",
                                            "Arial"]
        self._rcParams["axes.facecolor"] = "#E5E5E5"
        self._rcParams["axes.edgecolor"] = "bcbcbc"
        self._rcParams["axes.linewidth"] = "1"
        self._rcParams["axes.grid"] = "True"
        self._rcParams["axes.titlesize"] = "x-large"
        self._rcParams["axes.labelsize"] = "large"
        self._rcParams["axes.labelcolor"] = "black"
        self._rcParams["axes.axisbelow"] = "True"
        self._rcParams["axes.prop_cycle"] = cycler('color', ["#333333", "#348ABD", "#7A68A6",
                                             "#A60628", "#467821", "#CF4457", "#188487", "#E24A33"])
        self._rcParams["grid.color"] = "white"
        self._rcParams["grid.linewidth"] = "1.4"
        self._rcParams["grid.linestyle"] = "solid"
        self._rcParams["xtick.major.size"] = "0"
        self._rcParams["xtick.minor.size"] = "0"
        self._rcParams["xtick.major.pad"] = "6"
        self._rcParams["xtick.minor.pad"] = "6"
        self._rcParams["xtick.color"] = "#7F7F7F"
        self._rcParams["xtick.direction"] = "out"  # pointing out of axis
        self._rcParams["ytick.major.size"] = "0"
        self._rcParams["ytick.minor.size"] = "0"
        self._rcParams["ytick.major.pad"] = "6"
        self._rcParams["ytick.minor.pad"] = "6"
        self._rcParams["ytick.color"] = "#7F7F7F"
        self._rcParams["ytick.direction"] = "out"  # pointing out of axis
        self._rcParams["legend.fancybox"] = "True"
        self._rcParams["figure.figsize"] = "11, 8"
        self._rcParams["figure.facecolor"] = "1.0"
        self._rcParams["figure.edgecolor"] = "0.50"
        self._rcParams["figure.subplot.hspace"] = "0.5"

        # TODO: this slows down everything for some reason
        # self._rcParams["text.usetex"] = "True"

    def apply_final_touches(self, ax):
        '''Styles x,y axes to appear like ggplot2
        Must be called after all plot and axis manipulation operations have
        been carried out (needs to know final tick spacing)

        From: https://github.com/wrobstory/climatic/blob/master/climatic/stylers.py
        '''
        #Remove axis border
        for child in ax.get_children():
            if isinstance(child, mpl.spines.Spine):
                child.set_alpha(0)

        #Restyle the tick lines
        for line in ax.get_xticklines() + ax.get_yticklines():
            line.set_markersize(5)
            line.set_markeredgewidth(1.4)

        #Only show bottom left ticks
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        #Set minor grid lines
        ax.grid(True, 'minor', color='#F2F2F2', linestyle='-', linewidth=0.7)

        if not isinstance(ax.xaxis.get_major_locator(), mpl.ticker.LogLocator):
            ax.xaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(2))
        if not isinstance(ax.yaxis.get_major_locator(), mpl.ticker.LogLocator):
            ax.yaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(2))

class theme_bw(theme_gray):
    """
    White background w/ black gridlines
    """

    def __init__(self):
        super(theme_bw, self).__init__()
        self._rcParams['axes.facecolor'] = 'white'

class theme_xkcd(theme):
    """
    xkcd theme

    The theme internaly uses the settings from pyplot.xkcd().

    """
    def __init__(self, scale=1, length=100, randomness=2):
        super(theme_xkcd, self).__init__()
        with plt.xkcd(scale=scale, length=length, randomness=randomness):
            _xkcd = mpl.rcParams.copy()
        # no need to a get a deprecate warning for nothing...
        for key in mpl._deprecated_map:
            if key in _xkcd:
                del _xkcd[key]
        if 'tk.pythoninspect' in _xkcd:
                del _xkcd['tk.pythoninspect']
        self._rcParams.update(_xkcd)

    def __deepcopy__(self, memo):
        class _empty(object):
            pass
        result = _empty()
        result.__class__ = self.__class__
        result.__dict__["_rcParams"] = {}
        for k, v in self._rcParams.items():
            try:
                result.__dict__["_rcParams"][k] = deepcopy(v, memo)
            except NotImplementedError:
                # deepcopy raises an error for objects that are drived from or
                # composed of matplotlib.transform.TransformNode.
                # Not desirable, but probably requires upstream fix.
                # In particular, XKCD uses matplotlib.patheffects.withStrok
                # -gdowding
                result.__dict__["_rcParams"][k] = copy(v)
        return result
