from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .scale import scale
from copy import deepcopy


class scale_y_reverse(scale):
    """
    Reverse y axis

    Examples
    --------
    >>> ggplot(diamonds, aes(x='price')) + geom_histogram() + scale_y_reverse()
    """

    def __radd__(self, gg):
        gg = deepcopy(gg)
        gg.scale_y_reverse = True
        return gg


class scale_x_reverse(scale):
    """
    Reverse x axis

    Examples
    --------
    >>> ggplot(diamonds, aes(x='price')) + geom_histogram() + scale_x_reverse()
    """
    def __radd__(self, gg):
        gg = deepcopy(gg)
        gg.scale_x_reverse = True
        return gg
