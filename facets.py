import matplotlib.pyplot as plt
import numpy as np
import math

class facet_wrap(object):
    def __init__(self, x=None, y=None, nrow=None, ncol=None):
        self.x_var = x
        self.y_var = y
        self.nrow = nrow
        self.ncol = ncol

    def __radd__(self, gg):
        if gg.__class__.__name__=="ggplot":
            x, y = None, None
            ndim = None
            if self.x_var:
                x = gg.data[self.x_var]
                ndim = x.nunique()
            if self.y_var:
                y = gg.data[self.y_var]
                if ndim:
                    ndim *= y.nunique()
                else:
                    ndim = y.nunique()
            n_rows = self.nrow
            n_cols = self.ncol

            if self.nrow is None and self.ncol is None:
                # calculate both on the fly
                n_rows = math.ceil(math.sqrt(ndim))
                n_cols = math.ceil(ndim / math.ceil(math.sqrt(ndim)))
            elif self.nrow is None:
                # calculate n_rows on the fly
                n_rows = math.ceil(float(ndim) / n_cols)
            elif self.ncol is None:
                # calculate n_columns on the fly
                n_cols = math.ceil(float(ndim) / n_rows)

            gg.facets = {
                'row': self.x_var,
                'col': self.y_var,
                'n_rows': int(n_rows),
                'n_cols': int(n_cols),
                'ndim': int(ndim),
                'wrap': True
            }
            return gg

        return self

class facet_grid(object):
    def __init__(self, x=None, y=None):
        self.x_var = x
        self.y_var = y

    def __radd__(self, gg):
        if gg.__class__.__name__=="ggplot":
            x, y = None, None
            xdim, ydim = None, None
            ndim = None
            if self.x_var:
                x = gg.data[self.x_var]
                xdim = int(x.nunique())
            if self.y_var:
                y = gg.data[self.y_var]
                ydim = int(y.nunique())

            gg.facets = {
                'row': self.x_var,
                'col': self.y_var,
                'n_rows': xdim,
                'n_cols': ydim,
                'wrap': False
            }
            return gg
        return self
