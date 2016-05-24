from ggplot import *

p = ggplot(mtcars, aes('factor(cyl)', 'mpg'))
print p + geom_violin()



# import matplotlib.pyplot as plt
# from ggplot import mtcars
#
#
# f, ax = plt.subplots()
# ax.violinplot(mtcars.mpg)
#
# f.savefig("./violin.png", dpi=340)
