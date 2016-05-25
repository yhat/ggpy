from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .scale import scale
from copy import deepcopy


class scale_color_yhat(scale):
    """
    Use Yhat's color scheme.

    Examples
    --------
    >>> from ggplot import *
    >>> lng = pd.melt(meat, ['date'])
    >>> gg = ggplot(lng, aes('date', y='beef', color='variable')) + \\
    ...     geom_point() + scale_color_yhat()
    """
    VALID_SCALES = []
    def __radd__(self, gg):
        gg.manual_color_list = [
            "#428bca",
            "#5cb85c",
            "#5bc0de",
            "#f0ad4e",
            "#d9534f"
        ]
        return gg
