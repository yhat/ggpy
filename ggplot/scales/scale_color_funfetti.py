from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .scale import scale
from copy import deepcopy


class scale_color_funfetti(scale):
    """
    Make your plots look like funfetti

    Parameters
    ----------
    type: string
        One of confetti or sprinkles (defaults to sprinkles)

    Examples
    --------
    >>> from ggplot import *
    >>> p = ggplot(aes(x='carat', y='price', colour='clarity'), data=diamonds)
    >>> p += geom_point()
    >>> print(p + scale_color_funfetti())
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
        # try:
        #     color_col = gg._aes.data.get('color', gg._aes.data.get('fill'))
        #     n_colors = max(gg.data[color_col].nunique(), 3)
        # except:
        #     n_colors = 5

        gg.manual_color_list = color_maps.get(self.type, color_maps['sprinkles'])

        return gg
