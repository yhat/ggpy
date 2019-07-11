from __future__ import print_function
from ggplot import *
import pandas as pd
import numpy as np


df = pd.DataFrame([{"x":2,"y":1,"z":"1","w":4},{"x":5,"y":1,"z":"1","w":2},{"x":7,"y":1,"z":"2","w":2},{"x":9,"y":1,"z":"2","w":2},{"x":12,"y":1,"z":"3","w":4},{"x":2,"y":2,"z":"3","w":4},{"x":5,"y":2,"z":"4","w":2},{"x":7,"y":2,"z":"4","w":2},{"x":9,"y":2,"z":"5","w":2},{"x":12,"y":2,"z":"5","w":4}])
print(df.head())
p = ggplot(df, aes(xmin='x - w / 2', xmax='x + w / 2', ymin='y', ymax='y + 1', fill='z')) + geom_rect()
print(p)

p = ggplot(df, aes(xmin='x - w / 2', xmax='x + w / 2', ymin='y', ymax='y + 1', fill='z')) + geom_rect(color='black')
print(p)

p = ggplot(df, aes(xmin='x - w / 2', xmax='x + w / 2', ymin='y', ymax='y + 1', fill='z')) + \
    geom_rect(color='black') + \
    facet_wrap('w')
print(p)
