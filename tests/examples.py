from ggplot import *
import uuid
import seaborn as sns
import pandas as pd
import numpy as np
tips = sns.load_dataset('tips')
from datasets import mtcars, diamonds, pageviews
import sys


p = ggplot(mtcars, aes(x='mpg', y='cyl', color='steelblue')) + geom_point()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
p = ggplot(mtcars, aes(x='mpg', y='cyl')) + geom_point(color='green')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
p = ggplot(diamonds.sample(100), aes(x='carat', y='price')) + geom_point() + facet_wrap('clarity', ncol=4)
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
p = ggplot(diamonds.sample(100), aes(x='carat', y='price')) + geom_point() + facet_wrap('clarity', nrow=5)
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_grid(x='clarity')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_grid(y='clarity')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
p = ggplot(diamonds.sample(1000), aes(x='carat', y='price')) + geom_point() + facet_wrap(x='clarity', y='cut')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(x='clarity')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(y='clarity')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
p = ggplot(diamonds.sample(1000), aes(x='carat', y='price', size='clarity')) + geom_point()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
p = ggplot(diamonds.sample(1000), aes(x='carat', y='price', size='x')) + geom_point()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
p = ggplot(diamonds.sample(1000), aes(x='carat', y='price', alpha='x')) + geom_point()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
p = ggplot(diamonds.sample(1000), aes(x='carat', y='price', alpha='x')) + geom_point() + facet_grid(x='clarity')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
p = ggplot(diamonds.sample(1000), aes(x='carat', y='price', alpha='x')) + geom_point() + facet_grid(y='clarity')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")

# shape
p = ggplot(diamonds, aes(x='carat', y='price', shape='clarity')) + geom_point()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")

p = ggplot(diamonds.sample(100), aes(x='carat', y='price', shape='cut', color='clarity')) + geom_point() + scale_color_brewer() + facet_grid(x='color')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(diamonds.sample(100), aes(x='carat', y='price')) + geom_point() + scale_color_brewer() + facet_grid(x='color', y='clarity')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(diamonds.sample(100), aes(x='carat', y='price', shape='cut', color='clarity')) + geom_point() + scale_color_brewer() + facet_grid(y='color')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
p = ggplot(diamonds.sample(100), aes(x='carat', y='price', color='clarity')) + geom_point() + scale_color_brewer(type='div')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
p = ggplot(diamonds.sample(100), aes(x='carat', y='price', color='x')) + geom_point()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")


# # linetype
p = ggplot(diamonds.sample(100), aes(x='carat', y='price', linetype='cut')) + geom_line()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
#
# # histogram
p = ggplot(diamonds, aes(x='carat')) + geom_histogram()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # point
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # titles and stuff
p = ggplot(diamonds, aes(x='carat', y='price', color='clarity')) + geom_point() + xlab("THIS IS AN X LABEL") + ylab("THIS IS A Y LABEL") + ggtitle("THIS IS A TITLE")
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # density
p = ggplot(diamonds, aes(x='carat')) + geom_density()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # hline
p = ggplot(diamonds, aes(x='price')) + geom_hline(y=10)
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # vline
p = ggplot(diamonds, aes(x='price')) + geom_vline(x=10)
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # bar
p = ggplot(diamonds, aes(x='clarity')) + geom_bar()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # bar w/ weight
p = ggplot(diamonds, aes(x='clarity', weight='x')) + geom_bar()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # abline
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + geom_abline(slope=5000, intercept=-500)
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")

# abline w/ facet
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + geom_abline(slope=5000, intercept=-500) + facet_wrap(y='clarity')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")

# area
df = pd.DataFrame({"x": np.arange(1000)})
df['y_low'] = df.x * 0.9
df['y_high'] = df.x * 1.1
df['thing'] = ['a' if i%2==0 else 'b' for i in df.x]
p = ggplot(df, aes(x='x', ymin='y_low', ymax='y_high')) + geom_area()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
# # area w/ facet
p = ggplot(df, aes(x='x', ymin='y_low', ymax='y_high')) + geom_area() + facet_wrap(x='thing')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # facet wrap
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(x='clarity')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
# #
# # facet wrap w/ 2 variables
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(x='color', y='cut')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # facet grid w/ 1 variable
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_grid(x='color')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_grid(y='color')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # # facet grid w/ 2 variables
p = ggplot(diamonds, aes(x='price')) + geom_histogram() + facet_grid(x='color', y='cut')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
df = pd.DataFrame({"x": np.arange(100)})
df['y'] = df.x * 10
df['z'] = ["a" if x%2==0 else "b" for x in df.x]
#
# # polar coords
p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_polar()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # equal coords
p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_equal()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # equal coords faceted
p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_equal() + facet_wrap(x='z')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # flipped coords
p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_flip()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # flipped coords facted
p = ggplot(df, aes(x='x', y='y')) + geom_point() + coord_flip() + facet_grid(x='z')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # x dates formatting
p = ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line() + scale_x_date(labels=date_format('%B %-d, %Y'))
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # # x dates formatting faceted
pageviews['z'] = ["a" if i%2==0 else "b" for i in range(len(pageviews))]
p = ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line() + scale_x_date(labels=date_format('%B %-d, %Y')) + facet_grid(y='z')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # geom_line
p = ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # geom_line w/ facets
p = ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line() + facet_grid(y='z')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # stat_smooth w/ lm
p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth(method='lm')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # stat_smooth w/ lowess
p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth(method='lowess')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
# # stat_smooth w/ lowess and custom span
p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth(method='lowess', span=0.2)
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
#
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(x='color')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(y='color')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point()
p + scale_color_brewer(type='div')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + scale_color_manual(values=['pink', 'skyblue'])
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip', color='tip')) + geom_point() + scale_color_gradient(low='pink', high='royalblue')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() +  scale_x_log() + scale_y_log()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + scale_x_log() + scale_y_log() + facet_wrap(x='color')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + scale_x_reverse() + scale_y_reverse() + facet_wrap(x='color')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + scale_x_continuous(breaks=[0, 3, 6], labels=["Low", "Medium", "High"]) + scale_y_continuous(breaks=[0, 10000, 20000], labels=["Low", "Medium", "High"]) + facet_wrap(x='color')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + theme_gray()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + theme_xkcd()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point(color='orange')
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip', color='sex', shape='smoker', size='tip')) + geom_point()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + facet_wrap(x="time")
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + facet_wrap(y="time")
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + facet_wrap(x="time")
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point() + geom_line() + facet_wrap(x="time", y="smoker")
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")

p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() + facet_wrap(x="time", y="smoker")
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() + scale_color_brewer()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() + theme_538()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + xlim(low=10, high=25) + ylim(2, 12)
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + labs(x="this is x", y="this is y", title="this is title")
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + geom_vline(x=30) + geom_hline(y=10) + ylab("GOo!") + ggtitle("This is a title")
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + facet_wrap(x="time", y="smoker")
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_line(color="blue") + geom_point()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#k
p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_line(color="blue") + geom_point() + facet_wrap(x="time", y="smoker")
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill')) + geom_histogram()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill')) + geom_density()
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
#
p = ggplot(tips, aes(x='total_bill')) + geom_density() + facet_wrap(y="time")
p.save("./examples/example-" + str(uuid.uuid4()) + ".png")
