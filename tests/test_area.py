from __future__ import print_function
from ggplot import *
import pandas as pd


df = pd.melt(meat[['date', 'beef', 'veal', 'pork']], id_vars=['date']).dropna()
print(ggplot(df, aes(x='date', y='value', fill='variable')) + geom_area())
