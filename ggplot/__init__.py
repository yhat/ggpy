from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
# For testing purposes we might need to set mpl backend before any
# other import of matplotlib.
def _set_mpl_backend():
    import os
    import matplotlib as mpl

    env_backend = os.environ.get('MATPLOTLIB_BACKEND')
    if env_backend:
        # we were instructed
        mpl.use(env_backend)

_set_mpl_backend()

# This is the only place the version is specified and
# used in both setup.py and docs/conf.py to set the
# version of ggplot.
__version__ = '0.9.0'


from .geoms import geom_area, geom_blank, geom_boxplot, geom_line, geom_point, geom_jitter, geom_histogram, geom_density, geom_hline, geom_vline, geom_bar, geom_abline, geom_tile, geom_rect, geom_bin2d, geom_step, geom_text
from .geoms import stat_smooth, stat_density

from .facets import facet_wrap, facet_grid, Facet

from .chart_components import ggtitle, xlim, ylim, xlab, ylab, labs

from .ggplot import ggplot
from .qplot import qplot
from .aes import aes

from .coords.coords import coord_polar, coord_equal, coord_flip

from .datasets import chopsticks, diamonds, mtcars, meat, pageviews, pigeons, movies

from .scales.scale_color_brewer import scale_color_brewer
from .scales.scale_color_crayon import scale_color_crayon
from .scales.scale_color_funfetti import scale_color_funfetti
from .scales.scale_color_manual import scale_color_manual
from .scales.scale_color_gradient import scale_color_gradient
from .scales.scale_identity import scale_alpha_identity, scale_color_identity, scale_fill_identity, scale_linetype_identity, scale_shape_identity, scale_size_identity
from .scales.scale_log import scale_x_log, scale_y_log
from .scales.scale_reverse import scale_x_reverse, scale_y_reverse
from .scales.scale_x_continuous import scale_x_continuous
from .scales.scale_y_continuous import scale_y_continuous
from .scales.scale_x_discrete import scale_x_discrete
from .scales.scale_y_discrete import scale_y_discrete
from .scales.scale_x_date import scale_x_date
from .scales.scale_y_date import scale_y_date
from .scales.date_utils import date_format, date_breaks

from .themes import theme_538, theme_gray, theme_bw, theme_xkcd
