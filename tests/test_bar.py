from ggplot import *
import pandas as pd
import numpy as np
import sys

df = pd.DataFrame({
    'x': ['a', 'b', 'c', 'b', 'b', 'b', 'a', 'c', 'b', 'c', 'a'],
    'wt': [2, 3, 4, 10, 1, 1, 2, 10, 10, 4, 1],
    'thingy': ['hi','bye', 'hi', 'bye', 'bye', 'bye', 'bye', 'hi', 'bye', 'bye', 'bye'],
    'filler': ['limegreen', 'coral', 'coral', 'limegreen', 'limegreen', 'limegreen', 'coral', 'steelblue', 'steelblue', 'limegreen', 'steelblue']
})

p = ggplot(mtcars, aes(x='factor(cyl)', fill='factor(gear)')) + geom_bar(position='stack') + facet_wrap('vs')
print p
sys.exit()

p = ggplot(df, aes(x='x', weight='wt')) + geom_bar(color='teal') + scale_fill_identity()
print p

p = ggplot(df, aes(x='x', weight='wt', fill='filler')) + geom_bar() + scale_fill_identity()
print p


p = ggplot(df, aes(x='x', weight='wt', fill='filler')) + geom_bar(position='fill') + scale_fill_identity()
print p


# mtcars.cyl = mtcars.cyl.astype(str)
# mtcars.gear = mtcars.gear.astype(str)
p = ggplot(mtcars, aes(x='factor(cyl)', fill='factor(gear)')) + geom_bar(position='stack') + facet_wrap('vs')
print p

p = ggplot(mtcars, aes(x='factor(cyl)', fill='factor(gear)')) + geom_bar(position='stack') + facet_wrap('vs', 'am')
print p


# p = ggplot(mtcars, aes(x='factor(cyl)', fill='factor(gear)')) + geom_bar(position='fill')
# print p
#
# p = ggplot(df, aes(x='x', fill='filler')) + geom_bar(position='fill') + scale_fill_identity() + facet_wrap('thingy')
# print p

# p = ggplot(df, aes(x='x', fill='filler')) + geom_bar(position='fill') + facet_wrap('thingy')
# print p

# p = ggplot(mtcars, aes(x='factor(cyl)', fill='factor(gear)')) + geom_bar(position='fill')
# print p
#
# p = ggplot(mtcars, aes(x='factor(cyl)', fill='factor(vs)')) + geom_bar(position='fill')
# print p

# p = ggplot(df, aes(x='x', weight='wt', fill='filler')) + geom_bar() + scale_fill_identity()
# print p
#
# p = ggplot(df, aes(x='x', fill='filler')) + geom_bar() + scale_fill_identity()
# print p

# p = ggplot(df, aes(x='x', weight='wt')) + geom_bar()
# print p
#
# p = ggplot(df, aes(x='x')) + geom_bar()
# print p
# p = ggplot(diamonds, aes(x='clarity', fill='cut')) + geom_bar()
# print p
#
# p = ggplot(diamonds, aes(x='clarity', fill='cut')) + geom_bar(position='fill') + facet_wrap('cut')
# print p
