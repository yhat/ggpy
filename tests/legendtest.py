from __future__ import print_function
from ggplot import *

import pandas as pd
import numpy as np
from datasets import mtcars, diamonds, pageviews
from scales.scale_identity import scale_fill_identity


mtcars['newcol'] = ["steelblue" if i%2==0 else "coral" for i in range(len(mtcars))]
print(ggplot(mtcars, aes(x='mpg', fill='newcol')) + geom_histogram() + scale_fill_identity())
print(ggplot(mtcars, aes(x='wt', y='mpg', color='newcol', shape='newcol')) + geom_point())
print(ggplot(mtcars, aes(x='mpg', y='wt')) + geom_point(color='royalblue'))
print(ggplot(mtcars, aes(x='mpg', fill='factor(cyl)')) + geom_bar())
print(ggplot(mtcars, aes(x='mpg', y='wt', group='newcol')) + geom_line())

df = pd.DataFrame({"x": range(100), "y": range(100) })
df['newcol'] = ["steelblue" if i<25 else "coral" for i in range(len(df))]
print(ggplot(df, aes(x='x', y='y', group='newcol')) + geom_line())
