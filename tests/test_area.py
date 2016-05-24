from ggplot import *


print ggplot(meat, aes(x='date', y='beef')) + geom_area()
print ggplot(meat, aes(x='date', ymin='beef', ymax='pork')) + geom_ribbon()
