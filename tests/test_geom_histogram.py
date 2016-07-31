from ggplot import *


print ggplot(diamonds, aes(x='price')) + geom_histogram()
print ggplot(diamonds, aes(x='price')) + geom_histogram(bins=50)
