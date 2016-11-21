from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .scale import scale
from copy import deepcopy

class scale_y_continuous(scale):
    """
    Scale y axis as continuous values

    Parameters
    ----------
    breaks: list
        maps to ybreaks
    labels: list
        maps to ytick_labels

    Examples
    --------
    >>> print ggplot(mtcars, aes('mpg', 'qsec')) + \
    ...     geom_point() + \
    ...     scale_y_continuous(breaks=[10,20,30],  \
    ...     labels=["horrible", "ok", "awesome"])

    """
    VALID_SCALES = ['name', 'limits', 'labels', 'breaks', 'trans', 'ytick_formatter']
    def __radd__(self, gg):
        # gg = deepcopy(gg)
        if self.name:
            gg.ylab = self.name
        if not (self.limits is None):
            gg.ylimits = self.limits
        if not (self.breaks is None):
            gg.ybreaks = self.breaks
        if not (self.labels is None):
            gg.ytick_labels = self.labels
        if not (self.ytick_formatter is None):
            gg.ytick_formatter = self.ytick_formatter
        return gg
