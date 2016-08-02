from ggplot import *


diaa = diamonds[['cut','color','table']]
diab = diaa.groupby(['cut','color']).quantile([x/100.0 for x in range(0,100,5)])
diab.reset_index(inplace=True)
diab.columns = ['cut','color','p','stats']
# print ggplot(diab,aes(x='p', weight='stats')) + geom_bar() + facet_grid('color','cut')

print ggplot(diamonds, aes(x='clarity', weight='price')) + geom_bar() + facet_grid('color', 'cut')
print ggplot(diamonds, aes(x='clarity', weight='price', fill='color')) + geom_bar() + facet_grid('color', 'cut')
