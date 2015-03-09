from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import numpy as np

from .geom import geom


class geom_text(geom):
    DEFAULT_AES = {'alpha': None, 'angle': 0, 'color': 'black', 'family': None,
                   'fontface': 1, 'hjust': None, 'size': 12, 'vjust': None,
                   'lineheight': 1.2}
    REQUIRED_AES = {'label', 'x', 'y'}
    DEFAULT_PARAMS = {'stat': 'identity', 'position': 'identity',
                      'parse': False}

    _aes_renames = {'angle': 'rotation', 'lineheight': 'linespacing'}
    _units = {'alpha', 'color', 'family', 'size'}

    @staticmethod
    def draw(pinfo, scales, ax, **kwargs):
        x = pinfo.pop('x')
        y = pinfo.pop('y')
        label = pinfo.pop('label')
        # TODO: Deal with the fontface
        # from ggplot2
        # 1 = plain, 2 = bold, 3 = italic, 4 = bold italic
        # "plain", "bold", "italic", "oblique", and "bold.italic"
        pinfo.pop('fontface')

        if pinfo['hjust'] is not None:
            x = (np.array(x) + pinfo['hjust']).tolist()
        else:
            pinfo['horizontalalignment'] = 'center'

        if pinfo['vjust'] is not None:
            y = (np.array(y) + pinfo['vjust']).tolist()
        else:
            pinfo['verticalalignment'] = 'center'

        del pinfo['hjust']
        del pinfo['vjust']
        for x_g, y_g, s in zip(x, y, label):
            ax.text(x_g, y_g, s, **pinfo)
