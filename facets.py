import matplotlib.pyplot as plt
import numpy as np


#
# n_row = 3
# n_col = 2
#
# # sharex, sharey
# fig, subplots = plt.subplots(nrows=n_row, ncols=n_col, sharex=True, sharey=True)
#
#
# for row in range(n_row):
#     for col in range(n_col):
#         subplot = subplots[row][col]
#         subplot.set_title("%d - %d" % (row, col))
# plt.show()



class facet_grid(object):
    def __init__(self, x=None, y=None):
        self.x_var = x
        self.y_var = y

    def __radd__(self, other):
        if other.__class__.__name__=="ggplot":
            other.facets = { 'row': self.x_var, 'col': self.y_var, 'wrap': False}
            return other

        return self

class facet_wrap(object):
    def __init__(self, x=None, y=None):
        self.x_var = x
        self.y_var = y

    def __radd__(self, other):
        if other.__class__.__name__=="ggplot":
            other.facets = { 'row': self.x_var, 'col': self.y_var, 'wrap': True}
            return other

        return self
