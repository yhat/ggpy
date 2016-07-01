from ggplot import *
import pandas as pd


df = pd.melt(meat, id_vars=['date'])

print ggplot(df, aes(x='date', y='value', color='variable')) + geom_point()
