import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ggplot import ggplot
from aes import aes



class facet_wrap(object):
    def __init__(self, x=None, y=None):
        self.x_var = x
        self.y_var = y

    def __radd__(self, other):
        if isinstance(other, ggplot):
            other.grid = sns.FacetGrid(other.data, col=self.y_var,  row=self.x_var)
            return other

        return self

class geom(object):
    def __init__(self, **kwargs):
        self.layers = [self]
        self.params = kwargs

    def __radd__(self, other):
        if isinstance(other, ggplot):
            other.layers += self.layers
            return other

        self.layers.append(other)
        return self

class geom_point(geom):

    def plot(self, data, variables):
        sns.lmplot(variables['x'], variables['y'], data=data, hue=variables.get('color'), fit_reg=False)

    def grid(self, grid, variables):
        color = variables.get('color')
        grid.map(sns.lmplot, variables['x'], variables['y']) #, fit_reg=False)

class geom_line(geom):

    def plot(self, data, variables):
        x = data[variables['x']]
        y = data[variables['y']]
        plt.plot(x, y)

    def grid(self, grid, variables):
        grid.map(plt.plot, variables['x'], variables['y'])

class geom_hist(geom):

    def plot(self, data, variables):
        x = data[variables['x']]
        plt.hist(x)

    def grid(self, grid, variables):
        grid.map(plt.hist, variables['x'])


class geom_density(geom):

    def plot(self, data, variables):
        x = data[variables['x']]
        sns.distplot(x, hist=False, kde=True)

    def grid(self, grid, variables):
        grid.map(sns.distplot, variables['x'], hist=False, kde=True)

class geom_abline(geom):
    # harder than it seems...
    pass

class geom_hline(geom):

    def plot(self, data, variables):
        plt.axhline(self.params.get('y'))

    def grid(self, grid, variables):
        grid.map(plt.axhline, variables['y'])

class geom_vline(geom):

    def plot(self, data, variables):
        plt.axvline(self.params.get('x'))

    def grid(self, grid, variables):
        grid.map(plt.axvline, variables['x'])

class stat_smooth(geom):

    def plot(self, data, variables):
        sns.regplot(variables['x'], variables['y'], data=data)

    def grid(self, grid, variables):
        grid.map(sns.regplot, variables['x'], variables['y'])
