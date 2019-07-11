from __future__ import print_function
from ggplot import *


print(ggplot(meat, aes(x='date', y='beef')) + stat_smooth() + scale_x_date(labels=date_format('%Y')))
print(ggplot(meat, aes(x='date', y='beef')) + stat_smooth(method='ma', window=12) + scale_x_date(labels=date_format('%Y')))
