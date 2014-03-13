from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .geom import geom

import matplotlib.pyplot

if hasattr(matplotlib.pyplot, 'hist2d'):
    class stat_bin2d(geom):
        VALID_AES = {'x', 'y', 'fill'}
        REQUIRED_AES = {'x', 'y'}
        PARAMS = {'geom': None, 'position': 'identity',
                'bins': 30, 'drop': True}

        def plot(self, layer, ax):
            x = layer.pop('x')
            y = layer.pop('y')

            ax.hist2d(x, y, cmap=matplotlib.pyplot.cm.Blues, **layer)
else:
    def stat_bin2d(*args, **kwargs):
        import matplotlib
        print("stat_bin2d only works with newer matplotlib versions, but found only %s" %
              matplotlib.__version__)
