from __future__ import print_function
from ggplot import *

import pandas as pd
import numpy as np
from datasets import mtcars, diamonds, pageviews


# print ggplot(diamonds, aes(x='price')) + geom_histogram() + facet_wrap('cut')
print(ggplot(diamonds, aes(x='price', color='factor(cyl)')) + geom_boxplot())
