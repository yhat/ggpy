from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import matplotlib.image as mpimg
import os
import sys

from .geom import geom

_ROOT = os.path.abspath(os.path.dirname(__file__))


class geom_now_its_art(geom):
    """
    Put a bird on it!

    Parameters
    ----------
    alpha:
        transparency of bird

    Examples
    --------
    """
    DEFAULT_AES = {'alpha': 0.5}
    DEFAULT_PARAMS = {}

    def plot(self, ax, data, _aes):
        (data, _aes) = self._update_data(data, _aes)
        params = self._get_plot_args(data, _aes)
        img = mpimg.imread(os.path.join(_ROOT, 'bird.png'))
        ax.imshow(img, **params)
        sys.stderr.write("Put a bird on it!\n")
