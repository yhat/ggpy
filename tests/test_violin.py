from __future__ import print_function
from ggplot import *
import pandas as pd


p = ggplot(mtcars, aes('factor(cyl)', 'mpg'))
print(p + geom_violin())

diamonds['clarity'] = pd.Categorical(diamonds['clarity'], ordered=True,
                                     categories='I1 SI2 SI1 VS2 VS1 VVS2 VVS1 IF'.split())
print(ggplot(diamonds, aes(x='clarity', y='price')) + geom_violin())


# import matplotlib.pyplot as plt
# from ggplot import mtcars
#
#
# f, ax = plt.subplots()
# ax.violinplot(mtcars.mpg)
#
# f.savefig("./violin.png", dpi=340)
