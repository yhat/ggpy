from __future__ import print_function
import pandas as pd
from ggplot import *

diamonds['cut'] = pd.Categorical(diamonds['cut'], ordered=True,
                                 categories=['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
diamonds['clarity'] = pd.Categorical(diamonds['clarity'], ordered=True,
                                     categories='I1 SI2 SI1 VS2 VS1 VVS2 VVS1 IF'.split())

diaa = diamonds[['cut','color','table']]
diab = diaa.groupby(['cut','color']).quantile([x/100.0 for x in range(0,100,5)])
diab.reset_index(inplace=True)
diab.columns = ['cut','color','p','stats']
print(ggplot(diab,aes(x='p', weight='stats')) + geom_bar() + facet_grid('color','cut'))

print(ggplot(diamonds, aes(x='clarity', weight='price')) + geom_bar() + facet_grid('color', 'cut'))
print(ggplot(diamonds, aes(x='clarity', weight='price', fill='color')) + geom_bar() + facet_grid('color', 'cut'))

print(ggplot(diamonds, aes(x='clarity', y='price')) + geom_boxplot() + facet_wrap('cut'))
