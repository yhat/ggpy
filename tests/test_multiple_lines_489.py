from __future__ import print_function
from ggplot import *
import pandas as pd

df = pd.DataFrame({'a': range(0,3), 'b': range(1,4)})
df['x'] = df.index
df = pd.melt(df, id_vars='x')

print(df)
print(ggplot(aes(x='x', y='value', color='variable'), df) + geom_line() + geom_point())
