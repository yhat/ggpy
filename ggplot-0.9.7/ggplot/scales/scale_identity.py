from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from copy import deepcopy

class scale_identity(object):
    """
    Use the value that you've passed for an aesthetic in the plot without mapping
    it to something else. Classic example is if you have a data frame with a column
    that's like this:
          mycolor
        0    blue
        1     red
        2   green
        3    blue
        4     red
        5    blue
    And you want the actual points you plot to show up as blue, red, or green. Under
    normal circumstances, ggplot will generate a palette for these colors because it
    thinks they are just normal categorical variables. Using scale_identity will make
    it so ggplot uses the values of the field as the aesthetic mapping, so the points
    will show up as the colors you want.
    """
    VALID_SCALES = ["identity_type"]
    def __radd__(self, gg):
        gg = deepcopy(gg)
        gg.scale_identity.add(self.identity_type)
        return gg

class scale_alpha_identity(scale_identity):
    identity_type = "alpha"

class scale_color_identity(scale_identity):
    identity_type = "color"

class scale_fill_identity(scale_identity):
    identity_type = "fill"

class scale_linetype_identity(scale_identity):
    identity_type = "linetype"

class scale_shape_identity(scale_identity):
    identity_type = "shape"

class scale_size_identity(scale_identity):
    identity_type = "size"
