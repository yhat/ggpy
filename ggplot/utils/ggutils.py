from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

def ggsave(plot, filename, width=None, height=None):
    plot.make()
    w, h = plot.fig.get_size_inches()
    if width:
        w = width
    if height:
        h = height
    plot.fig.set_size_inches(w, h)
    plot.fig.savefig(filename)
