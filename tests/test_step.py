from ggplot import *
import numpy as np
import pandas as pd

p = ggplot(meat, aes(x='date', y='beef')) + geom_step()
print p


df = pd.DataFrame({
    "x": np.arange(1000),
    "y": np.random.choice([-1, 1], 1000),
    "z": np.random.choice(["Alpha", "Zalpha"], 1000)
})

df.y = df.y.cumsum()
p = ggplot(df, aes(x='x', y='y')) + geom_step()
print p

p = ggplot(df, aes(x='x', y='y', color='z')) + geom_step()
print p

p = ggplot(df, aes(x='x', y='y')) + geom_step() + facet_wrap("z")
print p
