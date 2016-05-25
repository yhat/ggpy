from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .scale import scale
from copy import deepcopy


class scale_fill_yhat(scale):
    """
    Use Yhat's color scheme.

    Examples
    --------
    >>> from ggplot import *
    >>> color_list = ['#FFAAAA', '#ff5b00', '#c760ff', '#f43605', '#00FF00',
    ...               '#0000FF', '#4c9085']
    >>> lng = pd.melt(meat, ['date'])
    >>> gg = ggplot(lng, aes('date', fill='variable')) + \\
    ...     geom_bar() + scale_fill_yhat()
    """
    VALID_SCALES = []
    def __radd__(self, gg):
        gg.manual_fill_list = [
            "#428bca",
            "#5cb85c",
            "#5bc0de",
            "#f0ad4e",
            "#d9534f"
        ]
        return gg
