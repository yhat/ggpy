from ggplot import *

import seaborn as sns
import pandas as pd
import numpy as np
tips = sns.load_dataset('tips')
from datasets import mtcars, diamonds, pageviews


p = ggplot(mtcars, aes(x='mpg')) + geom_histogram(fill='blue')
