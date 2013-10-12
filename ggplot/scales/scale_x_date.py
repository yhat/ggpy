from scale import scale
from copy import deepcopy
import matplotlib.dates as mdates


class scale_x_date(scale):
    # include all valid scale_x_continuous scales
    VALID_SCALES = ['name', 'labels', 'limits', 'breaks', 'trans']
    VALID_SCALES += ['breaks', 'minor_breaks']
    def __radd__(self, gg):
        gg = deepcopy(gg)
        if self.name:
            gg.xlab = self.name.title()
        if self.labels:
            gg.xtick_formatter = mdates.DateFormatter(self.labels)
        if self.limits:
            gg.xlimits = self.limits
        if self.breaks:
            gg.xbreaks = self.breaks
        return gg
