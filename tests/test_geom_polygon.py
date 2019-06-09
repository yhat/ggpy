from __future__ import print_function
from ggplot import *
import pandas as pd

df = pd.DataFrame({
    "x": [0, 1, 1, 0] + [5, 10, 10, 5],
    "y": [0, 0, 1, 1] + [10, 10, 20, 20],
    "g": ["a", "a", "a", "a"] + ["b", "b", "b", "b"]
})

print(ggplot(df, aes(x='x', y='y', fill='g')) + geom_polygon())
print(ggplot(df, aes(x='x', y='y', color='g')) + geom_polygon())
print(ggplot(df[df.g=="b"], aes(x='x', y='y')) + geom_polygon(alpha=0.25, linetype='dashed'))
