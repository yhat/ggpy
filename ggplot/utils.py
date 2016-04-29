import matplotlib.cbook as cbook
import numpy as np

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
