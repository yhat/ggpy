from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

class coord_polar(object):

    def __radd__(sefl, gg):
        gg.coords = "polar"
        return gg

class coord_equal(object):

    def __radd__(sefl, gg):
        gg.coords = "equal"
        return gg

class coord_flip(object):

    def __radd__(sefl, gg):
        gg.coords = "flip"
        return gg


class coord_cartesian(object):

    def __radd__(sefl, gg):
        gg.coords = "cartesian"
        return gg
