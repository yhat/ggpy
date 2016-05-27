from ggplot import *
import numpy as np
import pandas as pd


x = [np.NaN, 1, 2, np.NaN, 4, 5]
y = [0, 1, 2, 3, 4, 5]

df = pd.DataFrame(dict(x=x, y=y))


print ggplot(df, aes(x='x', y='y')) + geom_point()
print ggplot(df, aes(x='x', y='y')) + geom_line()
print ggplot(df, aes(x='x', y='y')) + geom_step()

print ggplot(df, aes(x='x')) + geom_histogram()
print ggplot(df, aes(x='x', weight='x')) + geom_histogram()
print ggplot(df, aes(x='x', weight='x')) + geom_density()
