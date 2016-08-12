from ggplot import *

print ggplot(diamonds, aes(x='pricee')) + geom_histogram()
