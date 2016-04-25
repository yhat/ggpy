from geoms import geom_area, geom_line, geom_point, geom_histogram, geom_density, geom_hline, geom_vline, geom_bar, geom_abline
from geoms import stat_smooth
from facets import facet_wrap, facet_grid
from chart_components import ggtitle, xlim, ylim, xlab, ylab, labs
from ggplot import ggplot
from themes import theme_538, theme_gray, theme_xkcd
from scales.scale_color_brewer import scale_color_brewer
from scales.scale_color_manual import scale_color_manual
from scales.scale_color_gradient import scale_color_gradient
from scales.scale_log import scale_x_log, scale_y_log
from scales.scale_reverse import scale_x_reverse, scale_y_reverse
from scales.scale_x_continuous import scale_x_continuous
from scales.scale_y_continuous import scale_y_continuous
from scales.scale_x_discrete import scale_x_discrete
from scales.scale_y_discrete import scale_y_discrete
from scales.scale_x_date import scale_x_date
from scales.scale_y_date import scale_y_date
from coords.coords import coord_polar, coord_equal, coord_flip
from scales.date_utils import date_format, date_breaks
from aes import aes

import seaborn as sns
import pandas as pd
import numpy as np
tips = sns.load_dataset('tips')
from datasets import diamonds, pageviews

# shape
p = ggplot(diamonds.sample(100), aes(x='carat', y='price', shape='cut', color='clarity')) + geom_point() + facet_grid(x='color')
p.make()
# # linetype
p = ggplot(diamonds.sample(100), aes(x='carat', y='price', linetype='cut')) + geom_line()
p.make()

# # histogram
# p = ggplot(diamonds, aes(x='carat')) + geom_histogram()
# p.make()
#
# # point
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point()
# p.make()
#
# # density
# p = ggplot(diamonds, aes(x='carat')) + geom_density()
# p.make()

# # hline
# p = ggplot(diamonds, aes(x='price')) + geom_hline(y=10)
# p.make()
#
# # vline
# p = ggplot(diamonds, aes(x='price')) + geom_vline(x=10)
# p.make()
#
# # bar
# p = ggplot(diamonds, aes(x='clarity')) + geom_bar()
# p.make()
#
# # bar w/ weight
# p = ggplot(diamonds, aes(x='clarity', weight='x')) + geom_bar()
# p.make()

# # abline
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + geom_abline(slope=5000, intercept=-500)
# p.make()
#
# # abline w/ facet
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + geom_abline(slope=5000, intercept=-500) + facet_wrap(y='clarity')
# p.make()

# # area
# df = pd.DataFrame({"x": np.arange(1000)})
# df['y_low'] = df.x * 0.9
# df['y_high'] = df.x * 1.1
# df['thing'] = ['a' if i%2==0 else 'b' for i in df.x]
# p = ggplot(df, aes(x='x', ymin='y_low', ymax='y_high')) + geom_area()
# p.make()
# # area w/ facet
# p = ggplot(df, aes(x='x', ymin='y_low', ymax='y_high')) + geom_area() + facet_wrap(x='thing')
# p.make()

# # facet wrap
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(x='clarity')
# p.make()
# #
# # facet wrap w/ 2 variables
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(x='color', y='cut')
# p.make()

# # facet grid w/ 1 variable
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_grid(x='color')
# p.make()
#
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_grid(y='color')
# p.make()
#
# # # facet grid w/ 2 variables
# p = ggplot(diamonds, aes(x='price')) + geom_histogram() + facet_grid(x='color', y='cut')
# p.make()

df = pd.DataFrame({"x": np.arange(100)})
df['y'] = df.x * 10
df['z'] = ["a" if x%2==0 else "b" for x in df.x]

# # polar coords
# p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_polar()
# p.make()

# # equal coords
# p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_equal()
# p.make()

# # equal coords faceted
# p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_equal() + facet_wrap(x='z')
# p.make()

# # flipped coords
# p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_flip()
# p.make()

# # flipped coords facted
# p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_flip() + facet_grid(x='z')
# p.make()

# # x dates formatting
# p = ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line() + scale_x_date(labels=date_format('%B %-d, %Y'))
# p.make()

# # # x dates formatting faceted
# pageviews['z'] = ["a" if i%2==0 else "b" for i in range(len(pageviews))]
# # p = ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line() + scale_x_date(labels=date_format('%B %-d, %Y')) + facet_grid(y='z')
# # p.make()
#
# # geom_line
# p = ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line()
# p.make()
#
# # geom_line w/ facets
# p = ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line() + facet_grid(y='z')
# p.make()

# # stat_smooth w/ lm
# p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth(method='lm')
# p.make()
#
# # stat_smooth w/ lowess
# p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth(method='lowess')
# p.make()
#
# # stat_smooth w/ lowess and custom span
# p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth(method='lowess', span=0.2)
# p.make()






# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(x='color')
# p.make()
#
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(y='color')
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point()
# p + scale_color_brewer(type='div')
# p.make()

# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + scale_color_manual(values=['pink', 'skyblue'])
# p.make()

# p = ggplot(tips, aes(x='total_bill', y='tip', color='tip')) + geom_point() + scale_color_gradient(low='pink', high='royalblue')
# p.make()

# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() +  scale_x_log() + scale_y_log()
# p.make()

# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + scale_x_log() + scale_y_log() + facet_wrap(x='color')
# p.make()

# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + scale_x_reverse() + scale_y_reverse() + facet_wrap(x='color')
# p.make()

# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + scale_x_continuous(breaks=[0, 3, 6], labels=["Low", "Medium", "High"]) + scale_y_continuous(breaks=[0, 10000, 20000], labels=["Low", "Medium", "High"]) + facet_wrap(x='color')
# p.make()

# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + theme_gray()
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + theme_xkcd()
# p.make()

# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point()
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point(color='orange')
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex', shape='smoker', size='tip')) + geom_point()
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + facet_wrap(x="time")
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + facet_wrap(y="time")
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + geom_line() + facet_wrap(x="time", y="smoker")
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() + facet_wrap(x="time", y="smoker")
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() + scale_color_brewer()
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() + theme_538()
# p.make()
#
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + xlim(low=10, high=25) + ylim(2, 12)
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + labs(x="this is x", y="this is y", title="this is title")
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + geom_vline(x=30) + geom_hline(y=10) + gg("Hello!!!!") + ylab("GOo!") + ggtitle("This is a title")
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + facet_wrap(x="time", y="smoker")
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_line(color="blue") + geom_point()
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_line(color="blue") + geom_point() + facet_wrap(x="time", y="smoker")
# p.make()
#
# p = ggplot(tips, aes(x='total_bill')) + geom_histogram()
# p.make()
#
# p = ggplot(tips, aes(x='total_bill')) + geom_density()
# p.make()
#
# p = ggplot(tips, aes(x='total_bill')) + geom_density() + facet_wrap(y="time")
# p.make()
#
#
#
# tips = sns.load_dataset('tips')
# variables = {'x': 'total_bill', 'y': 'tip'}
#
#
# p = geom_histogram()
# print p.layers
#
# g = sns.FacetGrid(tips, col="time",  row="smoker")
# for layer in p.layers:
#     layer.grid(g, variables)
# plt.show()
#
# p = geom_density()
# print p.layers
#
# g = sns.FacetGrid(tips, col="time",  row="smoker")
# for layer in p.layers:
#     # layer.plot(tips, variables)
#     layer.grid(g, variables)
# plt.show()
#
#
# p = geom_point() + geom_line(color="blue")
# print p.layers
#
# g = sns.FacetGrid(tips, col="time",  row="smoker")
# for layer in p.layers:
#     layer.grid(g, variables)
# plt.show()
#
# variables = {'x': 'x', 'y': 'y'}
# x = np.arange(-20, 20)
# df = pd.DataFrame({
#     "x": x,
#     "y": x**2
# })
#
# for layer in p.layers:
#     layer.plot(df, variables)
# plt.show()
