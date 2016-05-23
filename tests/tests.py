from ggplot import *

import seaborn as sns
import pandas as pd
import numpy as np
tips = sns.load_dataset('tips')
import sys


# p = ggplot(mtcars, aes(x='mpg', y='cyl', color='steelblue')) + geom_point()
# print p
# p = ggplot(mtcars, aes(x='mpg', y='cyl')) + geom_point(color='green')
# print p
# p = ggplot(diamonds.sample(100), aes(x='carat', y='price')) + geom_point() + facet_wrap('clarity', ncol=4)
# print p
# p = ggplot(diamonds.sample(100), aes(x='carat', y='price')) + geom_point() + facet_wrap('clarity', nrow=5)
# print p
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_grid(x='clarity')
# print p
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_grid(y='clarity')
# print p
# p = ggplot(diamonds.sample(1000), aes(x='carat', y='price')) + geom_point() + facet_wrap(x='clarity', y='cut')
# print p
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(x='clarity')
# print p
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(y='clarity')
# print p
#
# p = ggplot(diamonds.sample(1000), aes(x='carat', y='price', size='clarity')) + geom_point()
# print p
# p = ggplot(diamonds.sample(1000), aes(x='carat', y='price', size='x')) + geom_point()
# print p
# p = ggplot(diamonds.sample(1000), aes(x='carat', y='price', alpha='x')) + geom_point()
# print p
# p = ggplot(diamonds.sample(1000), aes(x='carat', y='price', alpha='x')) + geom_point() + facet_grid(x='clarity')
# print p
#
# p = ggplot(diamonds.sample(1000), aes(x='carat', y='price', alpha='x')) + geom_point() + facet_grid(y='clarity')
# print p
#
# # shape
# p = ggplot(diamonds, aes(x='carat', y='price', shape='clarity')) + geom_point()
# p.save("testing.png")
#
# p = ggplot(diamonds.sample(100), aes(x='carat', y='price', shape='cut', color='clarity')) + geom_point() + scale_color_brewer() + facet_grid(x='color')
# print """p = ggplot(diamonds.sample(100), aes(x='carat', y='price', shape='cut', color='clarity')) + geom_point() + scale_color_brewer() + facet_grid(x='color')""",  p
#
# p = ggplot(diamonds.sample(100), aes(x='carat', y='price')) + geom_point() + scale_color_brewer() + facet_grid(x='color', y='clarity')
# print """p = ggplot(diamonds.sample(100), aes(x='carat', y='price')) + geom_point() + scale_color_brewer() + facet_grid(x='color', y='clarity')""",  p
#
# p = ggplot(diamonds.sample(100), aes(x='carat', y='price', shape='cut', color='clarity')) + geom_point() + scale_color_brewer() + facet_grid(y='color')
# print """p = ggplot(diamonds.sample(100), aes(x='carat', y='price', shape='cut', color='clarity')) + geom_point() + scale_color_brewer() + facet_grid(y='color')""",  p
# p = ggplot(diamonds.sample(100), aes(x='carat', y='price', color='clarity')) + geom_point() + scale_color_brewer(type='div')
# print """p = ggplot(diamonds.sample(100), aes(x='carat', y='price', color='clarity')) + geom_point() + scale_color_brewer(type='div')""",  p
# p = ggplot(diamonds.sample(100), aes(x='carat', y='price', color='x')) + geom_point()
# print """p = ggplot(diamonds.sample(100), aes(x='carat', y='price', color='x')) + geom_point()""",  p
#
#
# # linetype
# p = ggplot(diamonds.sample(100), aes(x='carat', y='price', linetype='cut')) + geom_line()
# print """p = ggplot(diamonds.sample(100), aes(x='carat', y='price', linetype='cut')) + geom_line()""",  p
#
#
# # histogram
# p = ggplot(diamonds, aes(x='carat')) + geom_histogram()
# print """p = ggplot(diamonds, aes(x='carat')) + geom_histogram()""",  p
#
# # point
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point()
# print """p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point()""",  p
#
# # titles and stuff
# p = ggplot(diamonds, aes(x='carat', y='price', color='clarity')) + geom_point() + xlab("THIS IS AN X LABEL") + ylab("THIS IS A Y LABEL") + ggtitle("THIS IS A TITLE")
# print """p = ggplot(diamonds, aes(x='carat', y='price', color='clarity')) + geom_point() + xlab("THIS IS AN X LABEL") + ylab("THIS IS A Y LABEL") + ggtitle("THIS IS A TITLE")""",  p
#
# # density
# p = ggplot(diamonds, aes(x='carat')) + geom_density()
# print """p = ggplot(diamonds, aes(x='carat')) + geom_density()""",  p

# hline
p = ggplot(diamonds, aes(x='price')) + geom_hline(y=10)
print """p = ggplot(diamonds, aes(x='price')) + geom_hline(y=10)""",  p

# vline
p = ggplot(diamonds, aes(x='price')) + geom_vline(x=10)
print """p = ggplot(diamonds, aes(x='price')) + geom_vline(x=10)""",  p

# bar
p = ggplot(diamonds, aes(x='clarity')) + geom_bar()
print """p = ggplot(diamonds, aes(x='clarity')) + geom_bar()""",  p

# bar w/ weight
p = ggplot(diamonds, aes(x='clarity', weight='x')) + geom_bar()
print """p = ggplot(diamonds, aes(x='clarity', weight='x')) + geom_bar()""",  p

# abline
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + geom_abline(slope=5000, intercept=-500)
print """p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + geom_abline(slope=5000, intercept=-500)""",  p

# abline w/ facet
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + geom_abline(slope=5000, intercept=-500) + facet_wrap(y='clarity')
print """p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + geom_abline(slope=5000, intercept=-500) + facet_wrap(y='clarity')""",  p

# area
df = pd.DataFrame({"x": np.arange(1000)})
df['y_low'] = df.x * 0.9
df['y_high'] = df.x * 1.1
df['thing'] = ['a' if i%2==0 else 'b' for i in df.x]
# p = ggplot(df, aes(x='x', ymin='y_low', ymax='y_high')) + geom_area()
# print """p = ggplot(df, aes(x='x', ymin='y_low', ymax='y_high')) + geom_area()""",  p
# area w/ facet
p = ggplot(df, aes(x='x', ymin='y_low', ymax='y_high')) + geom_area() + facet_wrap(x='thing')
print """p = ggplot(df, aes(x='x', ymin='y_low', ymax='y_high')) + geom_area() + facet_wrap(x='thing')""",  p

# facet wrap
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(x='clarity')
print """p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(x='clarity')""",  p
#
# facet wrap w/ 2 variables
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(x='color', y='cut')
print """p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(x='color', y='cut')""",  p

# facet grid w/ 1 variable
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_grid(x='color')
print """p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_grid(x='color')""",  p

p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_grid(y='color')
print """p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_grid(y='color')""",  p

# # facet grid w/ 2 variables
p = ggplot(diamonds, aes(x='price')) + geom_histogram() + facet_grid(x='color', y='cut')
print """p = ggplot(diamonds, aes(x='price')) + geom_histogram() + facet_grid(x='color', y='cut')""",  p

df = pd.DataFrame({"x": np.arange(100)})
df['y'] = df.x * 10
df['z'] = ["a" if x%2==0 else "b" for x in df.x]

# polar coords
p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_polar()
print """p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_polar()""",  p

# equal coords
p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_equal()
print """p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_equal()""",  p

# equal coords faceted
p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_equal() + facet_wrap(x='z')
print """p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_equal() + facet_wrap(x='z')""",  p

# flipped coords
p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_flip()
print """p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_flip()""",  p

# flipped coords facted
p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_flip() + facet_grid(x='z')
print """p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_flip() + facet_grid(x='z')""",  p

# x dates formatting
p = ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line() + scale_x_date(labels=date_format('%B %-d, %Y'))
print """p = ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line() + scale_x_date(labels=date_format('%B %-d, %Y'))""",  p

# # x dates formatting faceted
pageviews['z'] = ["a" if i%2==0 else "b" for i in range(len(pageviews))]
# p = ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line() + scale_x_date(labels=date_format('%B %-d, %Y')) + facet_grid(y='z')
# print """p = ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line() + scale_x_date(labels=date_format('%B %-d, %Y')) + facet_grid(y='z')""",  p

# geom_line
p = ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line()
print """p = ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line()""",  p

# geom_line w/ facets
p = ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line() + facet_grid(y='z')
print """p = ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line() + facet_grid(y='z')""",  p

# stat_smooth w/ lm
p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth(method='lm')
print """p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth(method='lm')""",  p

# stat_smooth w/ lowess
p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth(method='lowess')
print """p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth(method='lowess')""",  p

# stat_smooth w/ lowess and custom span
p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth(method='lowess', span=0.2)
print """p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth(method='lowess', span=0.2)""",  p

#
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(x='color')
# print """p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(x='color')""",  p
#
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(y='color')
# print """p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(y='color')""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point()
# p + scale_color_brewer(type='div')
# print """p + scale_color_brewer(type='div')""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + scale_color_manual(values=['pink', 'skyblue'])
# print """p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + scale_color_manual(values=['pink', 'skyblue'])""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='tip')) + geom_point() + scale_color_gradient(low='pink', high='royalblue')
# print """p = ggplot(tips, aes(x='total_bill', y='tip', color='tip')) + geom_point() + scale_color_gradient(low='pink', high='royalblue')""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() +  scale_x_log() + scale_y_log()
# print """p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() +  scale_x_log() + scale_y_log()""",  p
#
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + scale_x_log() + scale_y_log() + facet_wrap(x='color')
# print """p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + scale_x_log() + scale_y_log() + facet_wrap(x='color')""",  p
#
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + scale_x_reverse() + scale_y_reverse() + facet_wrap(x='color')
# print """p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + scale_x_reverse() + scale_y_reverse() + facet_wrap(x='color')""",  p
#
# p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + scale_x_continuous(breaks=[0, 3, 6], labels=["Low", "Medium", "High"]) + scale_y_continuous(breaks=[0, 10000, 20000], labels=["Low", "Medium", "High"]) + facet_wrap(x='color')
# print """p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + scale_x_continuous(breaks=[0, 3, 6], labels=["Low", "Medium", "High"]) + scale_y_continuous(breaks=[0, 10000, 20000], labels=["Low", "Medium", "High"]) + facet_wrap(x='color')""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + theme_gray()
# print """p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + theme_gray()""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + theme_xkcd()
# print """p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + theme_xkcd()""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point()
# print """p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point()""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point(color='orange')
# print """p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point(color='orange')""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex', shape='smoker', size='tip')) + geom_point()
# print """p = ggplot(tips, aes(x='total_bill', y='tip', color='sex', shape='smoker', size='tip')) + geom_point()""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + facet_wrap(x="time")
# print """p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + facet_wrap(x="time")""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + facet_wrap(y="time")
# print """p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + facet_wrap(y="time")""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + facet_wrap(x="time")
# print """p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + facet_wrap(x="time")""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + geom_line() + facet_wrap(x="time", y="smoker")
# print """p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + geom_line() + facet_wrap(x="time", y="smoker")""",  p
# sys.exit(0)
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() + facet_wrap(x="time", y="smoker")
# print """p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() + facet_wrap(x="time", y="smoker")""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() + scale_color_brewer()
# print """p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() + scale_color_brewer()""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() + theme_538()
# print """p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() + theme_538()""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + xlim(low=10, high=25) + ylim(2, 12)
# print """p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + xlim(low=10, high=25) + ylim(2, 12)""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + labs(x="this is x", y="this is y", title="this is title")
# print """p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + labs(x="this is x", y="this is y", title="this is title")""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + geom_vline(x=30) + geom_hline(y=10) + ylab("GOo!") + ggtitle("This is a title")
# print """p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + geom_vline(x=30) + geom_hline(y=10) + ylab("GOo!") + ggtitle("This is a title")""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + facet_wrap(x="time", y="smoker")
# print """p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + facet_wrap(x="time", y="smoker")""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_line(color="blue") + geom_point()
# print """p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_line(color="blue") + geom_point()""",  p
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_line(color="blue") + geom_point() + facet_wrap(x="time", y="smoker")
# print """p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_line(color="blue") + geom_point() + facet_wrap(x="time", y="smoker")""",  p
#
# p = ggplot(tips, aes(x='total_bill')) + geom_histogram()
# print """p = ggplot(tips, aes(x='total_bill')) + geom_histogram()""",  p
#
# p = ggplot(tips, aes(x='total_bill')) + geom_density()
# print """p = ggplot(tips, aes(x='total_bill')) + geom_density()""",  p
#
# p = ggplot(tips, aes(x='total_bill')) + geom_density() + facet_wrap(y="time")
# print """p = ggplot(tips, aes(x='total_bill')) + geom_density() + facet_wrap(y="time")""",  p


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
