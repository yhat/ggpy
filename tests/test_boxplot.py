from __future__ import print_function
from ggplot import *

import pandas as pd


print(ggplot(mpg, aes(x='class', y='hwy')) + geom_boxplot() )
print(ggplot(mpg, aes(x='class', y='hwy')) + geom_boxplot() + facet_wrap('manufacturer'))
print(ggplot(diamonds, aes('pd.cut(carat, bins=10, labels=range(10))', 'price')) + geom_boxplot())

diamonds['clarity'] = pd.Categorical(diamonds['clarity'], ordered=True,
                                     categories='I1 SI2 SI1 VS2 VS1 VVS2 VVS1 IF'.split())
print(ggplot(diamonds, aes(x='clarity', y='price')) + geom_boxplot())

# plot with fill grouping:
ggplot(diamonds, aes("color", "price", fill = "cut")) + \
          geom_boxplot(aes(width = 0.6, spacing=0.02) ) + scale_y_log()

# this order should also work now (aes of the ggplot needs to be updated upon __radd__)
ggplot(diamonds, aes("color", "price")) + \
          geom_boxplot(aes(fill = "cut", width = 0.6, spacing=0.02,) ) + scale_y_log()


# draw lines and outliers with darker shades of `fill` given as a float:
ggplot(diamonds, aes("color", "price")) + \
                    geom_boxplot(aes(fill = "cut", color=0.75, outlier_color=0.75, width = 0.6, spacing=0.02) ) + scale_y_log()

# plotting from percentile summary
price_summary = diamonds.groupby(['color', 'cut']).quantile([0.0, 0.05, 0.25, 0.5, 0.75, 0.95, 1.0]).reset_index()
print(ggplot(price_summary, aes("color", "price", fill = "cut")) + 
          geom_boxplot(aes(width = 0.6, spacing=0.02, quantiles='level_2') ) + scale_y_log())
