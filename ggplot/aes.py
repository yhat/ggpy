from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from six.moves import UserDict

from copy import deepcopy
import difflib

from patsy.eval import EvalEnvironment

from . import utils

import numpy as np
import pandas as pd

class aes(UserDict):
    """
    Creates a dictionary that is used to evaluate
    things you're plotting. Most typically, this will
    be a column in a pandas DataFrame.

    Parameters
    -----------
    x : x-axis value
        Can be used for continuous (point, line) charts and for
        discrete (bar, histogram) charts.
    y : y-axis value
        Can be used for continuous charts only
    color (colour) : color of a layer
        Can be continuous or discrete. If continuous, this will be
        given a color gradient between 2 colors.
    shape : shape of a point
        Can be used only with geom_point
    size : size of a point or line
        Used to give a relative size for a continuous value
    alpha : transparency level of a point
        Number between 0 and 1. Only supported for hard coded values.
    ymin : min value for a vertical line or a range of points
        See geom_area, geom_ribbon, geom_vline
    ymax : max value for a vertical line or a range of points
        See geom_area, geom_ribbon, geom_vline
    xmin : min value for a horizonal line
        Specific to geom_hline
    xmax : max value for a horizonal line
        Specific to geom_hline
    slope : slope of an abline
        Specific to geom_abline
    intercept : intercept of an abline
        Specific to geom_abline

    Examples
    --------
    >>> aes(x='x', y='y')
    >>> aes('x', 'y')
    >>> aes(x='weight', y='height', color='salary')
    """

    DEFAULT_ARGS = ['x', 'y', 'color']

    def __init__(self, *args, **kwargs):
        if args:
            self.data = dict(zip(self.DEFAULT_ARGS, args))
        else:
            self.data = {}
        if kwargs:
            self.data.update(kwargs)
        if 'colour' in self.data:
            self.data['color'] = self.data['colour']
            del self.data['colour']

        self.legend = []
        self.__eval_env__ = EvalEnvironment.capture(1)

    def __deepcopy__(self, memo):
        '''deepcopy support for ggplot'''
        result = aes()
        for key, item in self.__dict__.items():
            # don't make a deepcopy of the env!
            if key == "__eval_env__":
                result.__dict__[key] = self.__dict__[key]
                continue
            try:
                result.__dict__[key] = deepcopy(self.__dict__[key], memo)
            except:
                print(key)
                raise

        return result

    def _evaluate_expressions(self, data):
        """
        Evaluates patsy expressions within the aesthetics. For example, 'x + 1'
        , 'factor(x)', or 'pd.cut(price, bins=10)')
        """
        for key, item in self.data.items():
            if item not in data:
                def factor(s, levels=None, labels=None):
                    return s.apply(str)

                env = EvalEnvironment.capture(eval_env=(self.__eval_env__ or 1)).with_outer_namespace({ "factor": factor, "pd": pd, "np": np })
                try:
                    new_val = env.eval(item, inner_namespace=data)
                    data[item] = new_val
                except:
                    msg = "Invalid column: '%s'" % str(item)
                    matches = difflib.get_close_matches(item, data.columns)
                    msg += "\ndid you mean one of the following:\n"
                    for match in matches:
                        msg += "    - %s\n" % match
                    raise Exception(msg)
        return data

    def handle_identity_values(self, df):
        for key, value in self.data.items():
            if value not in df.columns:
                df[value] = value
        return df

    def _get_discrete_aes(self, df):
        discrete_aes = []
        non_numeric_columns = df.select_dtypes(exclude=['number']).columns
        for aes_type, column in self.data.items():
            if aes_type in ['x', 'y']:
                continue
            elif aes_type=="group":
                discrete_aes.append((aes_type, column))
            elif column not in non_numeric_columns:
                continue
            else:
                discrete_aes.append((aes_type, column))

        return discrete_aes
