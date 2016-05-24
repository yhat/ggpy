from ggplot import *

print ggplot(mpg, aes(x='class', y='hwy')) + geom_boxplot()
print ggplot(mpg, aes(x='class', y='hwy')) + geom_boxplot() + facet_wrap('manufacturer')
