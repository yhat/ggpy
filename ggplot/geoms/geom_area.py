from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .geom import geom



class geom_area(geom):
    VALID_AES = {'x', 'ymin', 'ymax', 'color', 'alpha', 'label'}

    def plot(self, layer):
        x = layer.pop('x')
        y1 = layer.pop('ymin')
        y2 = layer.pop('ymax')
        ax.fill_between(x, y1, y2, **layer)

