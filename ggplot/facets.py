from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import math
import pprint as pp
from collections import OrderedDict

from .utils import sorted_unique

class Facet(object):
    def __init__(self, data, is_wrap, rowvar=None, colvar=None, nrow=None, ncol=None, scales=None):
        self.rowvar = rowvar
        self.colvar = colvar
        self.is_wrap = is_wrap
        self.nrow = nrow
        self.ncol = ncol
        self.facet_map = OrderedDict()
        self.scales = scales

        # if it's a facet_wrap, figure out how many rows and columns there should be
        # assign subplot indices to rowvars and columnvars
        self.ndim = ndim = self.calculate_ndimensions(data, rowvar, colvar)

        if is_wrap==True:
            if self.nrow:
                self.ncol = ncol = int(math.ceil(ndim / float(self.nrow)))
                self.nrow = nrow = int(self.nrow)
            elif self.ncol:
                self.nrow = nrow = int(math.ceil(ndim / float(self.ncol)))
                self.ncol = ncol = int(self.ncol)
            else:
                self.nrow = nrow = int(math.ceil(math.sqrt(ndim)))
                self.ncol = ncol = int(math.ceil(ndim / math.ceil(math.sqrt(ndim))))
        else:
            if rowvar:
                self.nrow = nrow = data[rowvar].nunique()
            else:
                self.nrow = nrow = 1
            if colvar:
                self.ncol = ncol = data[colvar].nunique()
            else:
                self.ncol = ncol = 1

        facet_values = self.generate_subplot_index(data, rowvar, colvar)
        for row in range(nrow):
            for col in range(ncol):
                try:
                    value = next(facet_values)
                except Exception as e:
                    continue
                if ncol==1:
                    self.facet_map[value] = (row, None)
                elif nrow==1:
                    self.facet_map[value] = (None, col)
                else:
                    self.facet_map[value] = (row, col)

    def generate_subplot_index(self, data, rowvar, colvar):
        if rowvar and colvar:
            for row in sorted_unique(data[rowvar]):
                for col in sorted_unique(data[colvar]):
                    yield (row, col)
        elif rowvar:
            for row in sorted_unique(data[rowvar]):
                yield row
        elif colvar:
            for col in sorted_unique(data[colvar]):
                yield col

    def calculate_ndimensions(self, data, rowvar, colvar):
        if rowvar and colvar:
            return data[rowvar].nunique() * data[colvar].nunique()
        elif rowvar:
            return data[rowvar].nunique()
        elif colvar:
            return data[colvar].nunique()
        else:
            raise Exception("No row or column specified to facet on!")

    @property
    def facet_cols(self):
        cols = []
        if self.rowvar:
            cols.append(self.rowvar)

        if self.colvar:
            cols.append(self.colvar)
        return cols

class facet_wrap(object):
    """
    Wrap panels from x and (optionally) y variables to create subplots.

    Parameters
    -----------
    x:
        x facet
    y:
        y facet
    nrow:
        number of rows in your final plot
    ncol:
        number of columns in your final plot
    scales:
        how individual panels x and y axes will be scaled. options are:
            "free" - x and y axis are different for each panel
            "free_y" - panels have same x axis but different y axis scales
            "free_x" - panels have same y axis but different x axis scales
            "fixed" - all panels are the same

    Examples
    --------
    """

    def __init__(self, x=None, y=None, nrow=None, ncol=None, scales=None):
        self.x_var = x
        self.y_var = y
        self.nrow = nrow
        self.ncol = ncol
        self.scales = scales

    def __radd__(self, gg):
        if gg.__class__.__name__=="ggplot":
            gg.facets = Facet(gg.data, True, self.x_var, self.y_var, nrow=self.nrow, ncol=self.ncol, scales=self.scales)
            return gg

        return self

class facet_grid(object):
    """
    Layout panels from x and (optionally) y variables in a grid format.

    Parameters
    -----------
    x:
        x facet
    y:
        y facet
    nrow:
        number of rows in your final plot
    ncol:
        number of columns in your final plot
    scales:
        how individual panels x and y axes will be scaled. options are:
            "free" - x and y axis are different for each panel
            "free_y" - panels have same x axis but different y axis scales
            "free_x" - panels have same y axis but different x axis scales
            "fixed" - all panels are the same

    Examples
    --------
    """
    def __init__(self, x=None, y=None, scales=None):
        self.x_var = x
        self.y_var = y
        self.scales = scales

    def __radd__(self, gg):
        if gg.__class__.__name__=="ggplot":
            gg.facets = Facet(gg.data, False, self.x_var, self.y_var, scales=self.scales)
            return gg
        return self
