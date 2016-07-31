from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .scale import scale
from copy import deepcopy


class scale_fill_funfetti(scale):
    """
    Make your plots look like funfetti

    Parameters
    ----------
    type: string
        One of confetti or sprinkles (defaults to sprinkles)
        
    Examples
    --------
    >>> from ggplot import *
    >>> p = ggplot(aes(x='carat', fill='clarity'), data=diamonds)
    >>> p += geom_bar()
    >>> print(p + scale_fill_funfetti())
    """
    VALID_SCALES = ['type', 'palette']

    def __radd__(self, gg):
        color_maps = {
            "confetti": [
                "#a864fd",
                "#29cdff",
                "#78ff44",
                "#ff718d",
                "#fdff6a"
            ],
            "sprinkles": [
                "#F8909F",
                "#C5DE9C",
                "#8BF3EF",
                "#F9AA50",
                "#EDE5D9"
            ]
        }
        gg.manual_fill_list = color_maps.get(self.type, color_maps['sprinkles'])

        return gg
