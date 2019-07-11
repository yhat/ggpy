from __future__ import print_function
from ggplot import *
import pandas as pd


print(ggplot(mpg, aes(x='class', y='hwy')) + geom_boxplot())
print(ggplot(mpg, aes(x='class', y='hwy')) + geom_boxplot() + facet_wrap('manufacturer'))
print(ggplot(diamonds, aes('pd.cut(carat, bins=10, labels=range(10))', 'price')) + geom_boxplot())

diamonds['clarity'] = pd.Categorical(diamonds['clarity'], ordered=True,
                                     categories='I1 SI2 SI1 VS2 VS1 VVS2 VVS1 IF'.split())
print(ggplot(diamonds, aes(x='clarity', y='price')) + geom_boxplot())
