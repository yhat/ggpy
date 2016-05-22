from ggplot import *


p = ggplot(diamonds.sample(1000), aes(x='carat', y='price')) + geom_point() + facet_grid('cut', scales='free')
print p

p = ggplot(diamonds.sample(1000), aes(x='carat', y='price')) + geom_point() + facet_grid('cut', scales='free_x')
print p

p = ggplot(diamonds.sample(1000), aes(x='carat', y='price')) + geom_point() + facet_grid('cut', scales='free_y')
print p

p = ggplot(diamonds.sample(1000), aes(x='carat', y='price')) + geom_point() + facet_wrap('cut', scales='free')
print p

p = ggplot(diamonds.sample(1000), aes(x='carat', y='price')) + geom_point() + facet_wrap('cut', scales='free_x')
print p

p = ggplot(diamonds.sample(1000), aes(x='carat', y='price')) + geom_point() + facet_wrap('cut', scales='free_y')
print p
