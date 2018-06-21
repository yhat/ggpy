from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import matplotlib.cbook as cbook
import numpy as np
import pandas as pd
import datetime


def format_ticks(ticks):
    are_ints = True
    for t in ticks:
        try:
            if int(t)!=t:
                are_ints = False
        except:
            return ticks

    if are_ints==True:
        return [int(t) for t in ticks]

    return ticks


def is_sequence_of_strings(obj):
    """
    Returns true if *obj* is iterable and contains strings
    """
    # Note: cbook.is_sequence_of_strings has a bug because
    # a numpy array of strings is recognized as being
    # string_like and therefore not a sequence of strings
    if not cbook.iterable(obj):
        return False
    if not isinstance(obj, np.ndarray) and cbook.is_string_like(obj):
        return False
    for o in obj:
        if not cbook.is_string_like(o):
            return False
    return True


def is_sequence_of_booleans(obj):
    """
    Return True if *obj* is array-like and contains boolean values
    """
    if not cbook.iterable(obj):
        return False
    _it = (isinstance(x, bool) for x in obj)
    if all(_it):
        return True
    return False


def is_categorical(obj):
    """
    Return True if *obj* is array-like and has categorical values

    Categorical values include:
        - strings
        - booleans
    """
    try:
        float(obj.iloc[0])
        return False
    except:
        return True

    if is_sequence_of_strings(obj):
        return True
    if is_sequence_of_booleans(obj):
        return True
    return False

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except:
        return False

date_types = (
    pd.Timestamp,
    pd.DatetimeIndex,
    pd.Period,
    pd.PeriodIndex,
    datetime.datetime,
    datetime.time
)

def is_date(x):
    return isinstance(x, date_types)

def calc_n_bins(series):
    "https://en.wikipedia.org/wiki/Histogram#Number_of_bins_and_width"
    q75, q25 = np.percentile(series, [75 , 25])
    iqr = q75 - q25
    h = (2 * iqr) / (len(series)**(1/3.))
    k = (series.max() - series.min()) / h
    return k

def sorted_unique(series):
    """Return the unique values of *series*, correctly sorted."""
    # This handles Categorical data types, which sorted(series.unique()) fails
    # on. series.drop_duplicates() is slower than Series(series.unique()).
    return list(pd.Series(series.unique()).sort_values())
