import matplotlib.pyplot as plt
import matplotlib as mpl
from aes import aes
import warnings
from themes import theme_gray

class ggplot(object):

    def __init__(self, obj1, obj2):
        self.layers = []
        self.grid = None
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

    def make(self):
        self.apply_scales()
        for layer in self.layers:
            if self.grid:
                layer.grid(self.grid, self._aes.data)
            else:
                layer.plot(self.data, self._aes.data)

        self.impose_limits()
        self.add_labels()
        self.apply_theme()

        plt.show()
