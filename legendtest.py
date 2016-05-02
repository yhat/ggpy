from ggplot import *

import pandas as pd
import numpy as np
from datasets import mtcars, diamonds, pageviews
from scales.scale_identity import scale_fill_identity


mtcars['newcol'] = ["steelblue" if i%2==0 else "coral" for i in range(len(mtcars))]
print ggplot(mtcars, aes(x='mpg', fill='newcol')) + geom_histogram() + scale_fill_identity()
# print ggplot(mtcars, aes(x='wt', y='mpg', color='newcol', shape='newcol')) + geom_point()
