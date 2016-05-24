from ggplot import *


print ggplot(diamonds, aes('carat', 'price')) + stat_smooth(method='lm')

print ggplot(diamonds, aes('price')) + stat_density()
