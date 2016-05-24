from ggplot import *


print ggplot(mpg, aes(x='class', y='hwy')) + geom_boxplot()
print ggplot(mpg, aes(x='class', y='hwy')) + geom_boxplot() + facet_wrap('manufacturer')

print ggplot(diamonds, aes('pd.cut(carat, bins=10, labels=range(10))', 'price')) + geom_boxplot()
