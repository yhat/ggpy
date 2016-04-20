from geoms import geom_line, geom_point, geom_hist, geom_density, geom_hline, geom_vline
from geoms import stat_smooth
from geoms import facet_wrap
from chart_components import ggtitle, xlim, ylim, xlab, ylab, labs
from ggplot import ggplot
from themes import theme_538
from scales.scale_color_brewer import scale_color_brewer
from aes import aes

import seaborn as sns
tips = sns.load_dataset('tips')


p = ggplot(tips, aes(x='total_bill', y='tip', color='size')) + geom_point() + facet_wrap(x="time")
p.make()

p = ggplot(tips, aes(x='total_bill', y='tip', color='sex')) + geom_point()
p.make()

p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point()
p.make()


# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() + scale_color_brewer()
# p.make()

# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_point() + theme_538()
# p.make()


# p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + xlim(low=10, high=25) + ylim(2, 12)
# p.make()

# p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + labs(x="this is x", y="this is y", title="this is title")
# p.make()

# p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + geom_vline(x=30) + geom_hline(y=10) + xlab("Hello!!!!") + ylab("GOo!") + ggtitle("This is a title")
# p.make()

# p = ggplot(tips, aes(x='total_bill', y='tip')) + stat_smooth() + facet_wrap(x="time", y="smoker")
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_line(color="blue") + geom_point()
# p.make()
#
# p = ggplot(tips, aes(x='total_bill', y='tip')) + geom_line(color="blue") + geom_point() + facet_wrap(x="time", y="smoker")
# p.make()
#
# p = ggplot(tips, aes(x='total_bill')) + geom_hist()
# p.make()
#
# p = ggplot(tips, aes(x='total_bill')) + geom_density()
# p.make()
#
# p = ggplot(tips, aes(x='total_bill')) + geom_density() + facet_wrap(y="time")
# p.make()



# tips = sns.load_dataset('tips')
# variables = {'x': 'total_bill', 'y': 'tip'}
#
#
# p = geom_hist()
# print p.layers
#
# g = sns.FacetGrid(tips, col="time",  row="smoker")
# for layer in p.layers:
#     layer.grid(g, variables)
# plt.show()
#
# p = geom_density()
# print p.layers
#
# g = sns.FacetGrid(tips, col="time",  row="smoker")
# for layer in p.layers:
#     # layer.plot(tips, variables)
#     layer.grid(g, variables)
# plt.show()

#
# p = geom_point() + geom_line(color="blue")
# print p.layers
#
# g = sns.FacetGrid(tips, col="time",  row="smoker")
# for layer in p.layers:
#     layer.grid(g, variables)
# plt.show()
#
# variables = {'x': 'x', 'y': 'y'}
# x = np.arange(-20, 20)
# df = pd.DataFrame({
#     "x": x,
#     "y": x**2
# })
#
# for layer in p.layers:
#     layer.plot(df, variables)
# plt.show()
