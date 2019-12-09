from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .date_utils import date_breaks, date_format
from .scale import scale
from copy import deepcopy
import six


class scale_y_date(scale):
    """
    Position scale, date

    Parameters
    ----------
    breaks : string / list of breaks
        1) a string specifying the width between breaks.
        2) the result of a valid call to `date_breaks`
        3) a vector of breaks (TODO: not implemented yet!)

    Examples
    --------
    >>> # 1) manually pass in breaks=date_breaks()
    >>> print(ggplot(meat, aes('beef','date')) + \\
    ...       geom_line() + \\
    ...       scale_y_date(breaks=date_breaks('10 years'),
    ...           labels=date_format('%B %-d, %Y')))
    >>> # 2) or breaks as just a string
    >>> print(ggplot(meat, aes('beef','date')) + \\
    ...       geom_line() + \\
    ...       scale_y_date(breaks='10 years',
    ...           labels=date_format('%B %-d, %Y')))
    """
    VALID_SCALES = ['name', 'labels', 'limits', 'breaks', 'trans']
    def __radd__(self, gg):
        gg = deepcopy(gg)
        if self.name:
            gg.ylab = self.name.title()
        if not (self.labels is None):
            if isinstance(self.labels, six.string_types):
                self.labels = date_format(self.labels)
            gg.ytick_formatter = self.labels
        if not (self.limits is None):
            gg.ylimits = self.limits
        if not (self.breaks is None):
            if isinstance(self.breaks, six.string_types):
                self.breaks = date_breaks(self.breaks)
            gg.ymajor_locator = self.breaks
        return gg

