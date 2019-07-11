from __future__ import print_function
from ggplot import *

print(ggplot(diamonds, aes(x='pricee')) + geom_histogram())
