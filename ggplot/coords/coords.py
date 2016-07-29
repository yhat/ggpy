from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

class coord_polar(object):
    """
    Use polar coordinates for plot
    """
    def __radd__(sefl, gg):
        gg.coords = "polar"
        return gg

class coord_equal(object):
    """
    Make x and y axes have equal scales
    """

    def __radd__(sefl, gg):
        gg.coords = "equal"
        return gg

class coord_flip(object):
    """
    Swap x and y coordinates
    """
    def __radd__(sefl, gg):
        gg.coords = "flip"
        return gg

class coord_cartesian(object):
    """
    Use cartesian coordinate system (this is default)
    """
    def __radd__(sefl, gg):
        gg.coords = "cartesian"
        return gg
