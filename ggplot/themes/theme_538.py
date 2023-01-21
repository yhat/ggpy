from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .theme import theme_base

class theme_538(theme_base):
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
