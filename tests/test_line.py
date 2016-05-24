from ggplot import *
import pandas as pd
import numpy as np
import random

x = np.arange(100)
random.shuffle(x)

df = pd.DataFrame({
    'x': x,
    'y': np.arange(100)
})

print ggplot(df, aes(x='x', y='y')) + geom_line()
print ggplot(df, aes(x='x', y='y')) + geom_path()
