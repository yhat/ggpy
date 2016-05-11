from ggplot import *

p = ggplot(meat, aes(x='date', y='beef')) + geom_point()
print p
