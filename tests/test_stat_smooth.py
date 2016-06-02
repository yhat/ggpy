from ggplot import *


print ggplot(meat, aes(x='date', y='beef')) + stat_smooth() + scale_x_date(labels=date_format('%Y'))
