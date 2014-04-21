import sys
import numpy as np
from matplotlib.colors import rgb2hex
from ..utils.color import ColorHCL
from .colors import hue_pal, color_gen
from copy import deepcopy
import six


def assign_fills(data, aes, gg):
    """
    Assigns colors to the given data based on the aes and adds the right legend

    We need to take a value an convert it into colors that we can actually
    plot. This means checking to see if we're colorizing a discrete or
    continuous value, checking if their is a fillmap, etc.

    Parameters
    ----------
    data : DataFrame
        dataframe which should have shapes assigned to
    aes : aesthetic
        mapping, including a mapping from color to variable
    gg : ggplot object, which holds information and gets a legend assigned

    Returns
    -------
    data : DataFrame
        the changed dataframe
    """
    if 'fill' in aes:
        fill_col = aes['fill']
        # Handle continuous colors here. We're going to use whatever fillmap
        # is defined to evaluate for each value. We're then going to convert
        # each color to HEX so that it can fit in 1 column. This will make it
        # much easier when creating layers. We're also going to evaluate the 
        # quantiles for that particular column to generate legend scales. This
        # isn't what ggplot does, but it's good enough for now.
        if fill_col in data._get_numeric_data().columns:
            values = data[fill_col].tolist()
            # Normalize the values for the fillmap
            values = [(i - min(values)) / (max(values) - min(values)) for i in values]
            fill_mapping = gg.fillmap(values)[::, :3]
            data["fill_mapping"] = [rgb2hex(value) for value in fill_mapping]
            quantiles = np.percentile(gg.data[fill_col], [0, 25, 50, 75, 100])
            key_colors = gg.fillmap([0, 25, 50, 75, 100])[::, :3]
            key_colors = [rgb2hex(value) for value in key_colors]
            gg.add_to_legend("fill", dict(zip(key_colors, quantiles)), scale_type="continuous")

        # Handle discrete colors here. We're going to check and see if the user
        # has defined their own color palette. If they have then we'll use those
        # colors for mapping. If not, then we'll generate some default colors.
        # We also have to be careful here because for some odd reason the next()
        # function is different in Python 2.7 and Python 3.0. Once we've done that
        # we generate the legends based off the the (color -> value) mapping.
        else:
            possible_fills = np.unique(data[fill_col])
            if gg.manual_fill_list:
                color = color_gen(len(possible_fills), gg.manual_fill_list)
            else:
                color = color_gen(len(possible_fills))
            fill_mapping = dict((value, six.next(color)) for value in possible_fills)
            data["fill_mapping"] = data[fill_col].apply(lambda x: fill_mapping[x])
            gg.add_to_legend("fill", dict((v, k) for k, v in fill_mapping.items()))

    return data
