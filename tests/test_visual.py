from __future__ import print_function
from ggplot import *
import os
import string
import datetime
import pandas as pd
import numpy as np
import random


np.random.seed(10)
random.seed(10)

html = """
<html>
    <head>
        <style>
            img {
                max-width: 40%;
            }
        </style>
    </head>
    <body>
"""

run_id = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
html += "\n\t\t<h1>%s</h1>" % run_id
os.mkdir(os.path.join("/tmp/", run_id))

def make_filename_safe(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_') # I don't like spaces in filenames.
    return filename

def test(description, plot):
    global html
    filename = os.path.join("/tmp/", run_id, make_filename_safe(description + ".png"))
    plot.save(filename)
    div ="<div><p>{desc}</p><img src='{img_src}' /></div>".format(desc=description, img_src=filename)
    html += "\n\t\t" + div
    return div

# geom_point tests
test("geom_point x, y", ggplot(mpg, aes(x='cty', y='hwy')) + geom_point())
test("geom_point x, y, color", ggplot(mpg, aes(x='cty', y='hwy', color='manufacturer')) + geom_point())
test("geom_point x, y, shape", ggplot(mpg, aes(x='cty', y='hwy', shape='manufacturer')) + geom_point())
test("geom_point x, y, alpha", ggplot(mpg, aes(x='cty', y='hwy', alpha='year')) + geom_point())
test("geom_point x, y, alpha parameter", ggplot(mpg, aes(x='cty', y='hwy')) + geom_point(alpha=0.25))

# geom_line vs. geom_step tests
x = np.arange(100)
random.shuffle(x)

df = pd.DataFrame({ 'x': x, 'y': np.arange(100) })
test("geom_line basic", ggplot(df, aes(x='x', y='y')) + geom_line())
test("geom_step basic", ggplot(df, aes(x='x', y='y')) + geom_path())

# geom_histogram
test("geom_histogram basic", ggplot(diamonds, aes(x='price')) + geom_histogram())
test("geom_histogram bins parameter", ggplot(diamonds, aes(x='price')) + geom_histogram(bins=50))
test("geom_histogram fill", ggplot(diamonds, aes(x='price', fill='clarity')) + geom_histogram())
test("geom_histogram color", ggplot(diamonds, aes(x='price', color='clarity')) + geom_histogram())

# geom_polygon
df = pd.DataFrame({
    "x": [0, 1, 1, 0] + [5, 10, 10, 5],
    "y": [0, 0, 1, 1] + [10, 10, 20, 20],
    "g": ["a", "a", "a", "a"] + ["b", "b", "b", "b"]
})

test("geom_polygon basic", ggplot(df[df.g=="a"], aes(x='x', y='y')) + geom_polygon())
test("geom_polygon fill", ggplot(df, aes(x='x', y='y', fill='g')) + geom_polygon())
test("geom_polygon color", ggplot(df, aes(x='x', y='y', color='g')) + geom_polygon())
test("geom_polygon with alpha parameter", ggplot(df[df.g=="b"], aes(x='x', y='y')) + geom_polygon(alpha=0.25))
test("geom_polygon linetype and size parameters", ggplot(df, aes(x='x', y='y', color='g')) + geom_polygon(linetype='dashed', size=10))

# geom_errorbar
test("geom_errorbar basic", ggplot(mpg, aes(x='class', y='hwy')) + geom_errorbar())
test("geom_errorbar color (doesn't work)", ggplot(mpg, aes(x='class', y='hwy', color='manufacturer')) + geom_errorbar())

# geom_boxplot
test("geom_boxplot basic", ggplot(mpg, aes(x='class', y='hwy')) + geom_boxplot())
test("geom_boxplot with patsy", ggplot(diamonds, aes('pd.cut(carat, bins=10, labels=range(10))', 'price')) + geom_boxplot())

# geom_rect
df = pd.DataFrame([{"x":2,"y":1,"z":"1","w":4},{"x":5,"y":1,"z":"1","w":2},{"x":7,"y":1,"z":"2","w":2},{"x":9,"y":1,"z":"2","w":2},{"x":12,"y":1,"z":"3","w":4},{"x":2,"y":2,"z":"3","w":4},{"x":5,"y":2,"z":"4","w":2},{"x":7,"y":2,"z":"4","w":2},{"x":9,"y":2,"z":"5","w":2},{"x":12,"y":2,"z":"5","w":4}])
p = ggplot(df, aes(xmin='x - w / 2', xmax='x + w / 2', ymin='y', ymax='y + 1', fill='z')) + geom_rect()
test("geom_rect with fill", p)

p = ggplot(df, aes(xmin='x - w / 2', xmax='x + w / 2', ymin='y', ymax='y + 1', fill='z')) + geom_rect(color='black')
test("geom_rect with fill and color parameter", p)

# geom_violin
test("geom_violin basic", ggplot(mtcars, aes('factor(cyl)', 'mpg')) + geom_violin())

df = pd.DataFrame(dict(
    x=np.random.normal(0, 1, 1000),
    y=np.random.normal(0, 1, 1000),
    w=np.random.uniform(-1, 1, 1000)
))
test("geom_tile with interpolate", ggplot(df, aes(x='x', y='y', fill='w')) + geom_tile(interpolate=True))
# test("geom_bin2d with fill", ggplot(df, aes(x='x', y='y', fill='w')) + geom_bin2d())
# test("geom_tile with xbins", ggplot(df, aes(x='x', y='y', fill='w')) + geom_tile(xbins=5))
# test("geom_tile with ybins", ggplot(df, aes(x='x', y='y', fill='w')) + geom_tile(ybins=5))
# test("geom_tile with xbins and ybins", ggplot(df, aes(x='x', y='y', fill='w')) + geom_tile(xbins=8, ybins=10))

# geom_text
test("geom_text basic", ggplot(mtcars, aes(x='wt', y='mpg', label='name')) + geom_text())
test("geom_text with color", ggplot(mtcars, aes(x='wt', y='mpg', label='name', color='factor(cyl)')) + geom_text())

# test nans
x = [np.NaN, 1, 2, np.NaN, 4, 5]
y = [0, 1, 2, 3, 4, 5]

df = pd.DataFrame(dict(x=x, y=y))


test("nan geom_point", ggplot(df, aes(x='x', y='y')) + geom_point())
test("nan geom_line", ggplot(df, aes(x='x', y='y')) + geom_line())
test("nan geom_step", ggplot(df, aes(x='x', y='y')) + geom_step())
test("nan geom_histogram", ggplot(df, aes(x='x')) + geom_histogram())
test("nan geom_histogram with weight", ggplot(df, aes(x='x', weight='x')) + geom_histogram())
test("nan geom_density with weight", ggplot(df, aes(x='x', weight='x')) + geom_density())

# geom_bar
df = pd.DataFrame({
    'x': ['a', 'b', 'c', 'b', 'b', 'b', 'a', 'c', 'b', 'c', 'a'],
    'wt': [2, 3, 4, 10, 1, 1, 2, 10, 10, 4, 1],
    'thingy': ['hi','bye', 'hi', 'bye', 'bye', 'bye', 'bye', 'hi', 'bye', 'bye', 'bye'],
    'filler': ['limegreen', 'coral', 'coral', 'limegreen', 'limegreen', 'limegreen', 'coral', 'steelblue', 'steelblue', 'limegreen', 'steelblue']
})

test("geom_bar stack", ggplot(mtcars, aes(x='factor(cyl)', fill='factor(gear)')) + geom_bar(position='stack'))
test("geom_bar fill identity", ggplot(df, aes(x='x', weight='wt')) + geom_bar(color='teal') + scale_fill_identity())
test("geom_bar weight and fill with identity fill", ggplot(df, aes(x='x', weight='wt', fill='filler')) + geom_bar() + scale_fill_identity())
test("geom_bar weight with fill position", ggplot(df, aes(x='x', weight='wt', fill='filler')) + geom_bar(position='fill') + scale_fill_identity())
test("geom_bar factor x and fill", ggplot(mtcars, aes(x='factor(cyl)', fill='factor(gear)')) + geom_bar(position='fill'))

# geom_now_its_art
test("geom_now_its_art", ggplot(diamonds, aes('price')) + geom_now_its_art())

# facet_wrap
test("facet_wrap basic", ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(x='clarity'))
test("facet_wrap 2 variables",  ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + facet_wrap(x='color', y='cut'))
test("facet_wrap with equal coords", ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + coord_equal() + facet_wrap(x='color', y='cut'))
# test("facet_wrap with abline", ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + geom_abline(slope=5000, intercept=-500) + facet_wrap(y='clarity'))
test("facet_wrap with continuous x and y scales", ggplot(diamonds, aes(x='carat', y='price')) + geom_point() + scale_x_continuous(breaks=[0, 3, 6], labels=["Low", "Medium", "High"]) + scale_y_continuous(breaks=[0, 10000, 20000], labels=["Low", "Medium", "High"]) + facet_wrap(x='color'))

# facet_grid
# test("facet_grid with 1 variable", ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line() + facet_grid(y='z'))
# test("facet_grid with x date formatting", ggplot(pageviews, aes(x='date_hour', y='pageviews')) + geom_line() + scale_x_date(labels=date_format('%B %-d, %Y')) + facet_grid(y='z'))
test("facet_grid with color brewer", ggplot(diamonds, aes(x='carat', y='price', shape='cut', color='clarity')) + geom_point() + scale_color_brewer() + facet_grid(x='color'))

html += "\n\t</body>\n</html>"
print(html)
