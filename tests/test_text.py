from ggplot import *

p = ggplot(mtcars, aes(x='wt', y='mpg', label='name', color='factor(cyl)')) + geom_text()

print p
print p + geom_point()

# import matplotlib.pyplot as plt
# from ggplot import mtcars
# f, ax = plt.subplots()
#
#
# for _, row in mtcars.iterrows():
#     label = row.to_dict()['name']
#     ax.text(row.wt, row.mpg, label)
#
#
# f.savefig("./text.png", dpi=340)
