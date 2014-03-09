from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from copy import deepcopy
from ggplot.components import aes
from pandas import DataFrame

__ALL__ = ["geom"]

class geom(object):
    """Base class of all Geoms"""
    VALID_AES = set()
    REQUIRED_AES = set()
    data = None
    aes = None
    def __init__(self, *args, **kwargs):
        # new dict for each geom
        self.aes = {}
        for arg in args:
            if isinstance(arg, aes):
                for k, v in arg.items():
                    if k in self.VALID_AES:
                        self.aes[k] = v
            elif isinstance(arg, DataFrame):
                self.data = arg
            else:
                raise Exception('Unknown argument of type "{0}".'.format(type(arg)))
        if "data" in kwargs:
            self.data = kwargs.pop("data")
        if "mapping" in kwargs:
            for k, v in kwargs.pop("mapping").items():
                if k in self.VALID_AES:
                    self.aes[k] = v
        if "colour" in kwargs:
            kwargs["color"] = kwargs["colour"]
            del kwargs["colour"]

        self.manual_aes = {}
        for k, v in kwargs.items():
            if k in self.VALID_AES:
                self.manual_aes[k] = v

    def plot_layer(self, layer):
        layer = dict((k, v) for k, v in layer.items() if k in self.VALID_AES)
        layer.update(self.manual_aes)

        self._verify_aesthetics(layer)
        return self.plot(layer)

    def __radd__(self, gg):
        gg = deepcopy(gg)
        gg.geoms.append(self)
        return gg

    def _verify_aesthetics(self, layer):
        """
        Check if all the required aesthetics have been specified

        Raise an Exception if an aesthetic is missing
        """
        missing_aes = self.REQUIRED_AES - set(layer)
        if missing_aes:
            msg = '{} requires the following missing aesthetics: {}'
            raise Exception(msg.format(
                self.__class__.__name__, ', '.join(missing_aes)))
