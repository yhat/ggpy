from ggplot import *


print ggplot(meat, aes(x='date', y='beef')) + geom_area() + scale_x_date(labels='%Y')
print ggplot(meat, aes(x='date', ymin='beef', ymax='pork')) + geom_ribbon()
