from ggplot import *
import pandas as pd
import numpy as np


df = pd.DataFrame(dict(
    x=np.random.normal(0, 1, 1000),
    y=np.random.normal(0, 1, 1000),
    w=np.random.uniform(-1, 1, 1000)
))
print df.head()
p = ggplot(df, aes(x='x', y='y', fill='w')) + geom_tile()
print p

p = ggplot(df, aes(x='x', y='y', fill='w')) + geom_bin2d()
print p

p = ggplot(df, aes(x='x', y='y', fill='w')) + geom_tile(xbins=5)
print p

p = ggplot(df, aes(x='x', y='y', fill='w')) + geom_tile(ybins=5)
print p

p = ggplot(df, aes(x='x', y='y', fill='w')) + geom_tile(xbins=8, ybins=10)
print p
