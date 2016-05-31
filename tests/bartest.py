from ggplot import *
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "x": np.random.choice(range(2001, 2008), 250),
    "w": np.random.uniform(50, 400, 250),
    "cat": np.random.choice(["A", "B", "C", "D", "E"], 250)
})


p = ggplot(df, aes(x='x', weight='w', fill='cat')) + geom_bar() + theme_bw()
p.save('/tmp/grouped-bar.png')
