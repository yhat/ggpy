from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .scale import scale
from copy import deepcopy


class scale_y_log(scale):
    """
    Make y axis log based

    Parameters
    ----------
    base:
        log base to use (defaults to 10)

    Examples
    --------
    >>> ggplot(diamonds, aes(x='price')) + geom_histogram() + scale_y_log()
    >>> ggplot(diamonds, aes(x='price')) + geom_histogram() + scale_y_log(base=2)
    """
    def __init__(self, base=10):
        self.base = base

    def __radd__(self, gg):
        gg = deepcopy(gg)
        gg.scale_y_log = self.base
        return gg


class scale_x_log(scale):
    """
    Make x axis log based

    Parameters
    ----------
    base:
        log base to use (defaults to 10)

    Examples
    --------
    >>> ggplot(diamonds, aes(x='price', y='carat')) + geom_point() + scale_x_log()
    >>> ggplot(diamonds, aes(x='price', y='carat')) + geom_point() + scale_x_log(base=2)
    """

    def __init__(self, base=10):
        self.base = base

    def __radd__(self, gg, base=10):
        gg = deepcopy(gg)
        gg.scale_x_log = self.base
        return gg
