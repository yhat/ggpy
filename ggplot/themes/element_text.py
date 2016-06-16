from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from matplotlib.text import Text

FACES = ["plain", "italic", "bold", "bold.italic"]

class element_text(object):
    def __init__(self, text, family=None, face=None, color=None, size=None,
            hjust=0, vjust=0, angle=None, lineheight=None, margin=None,
            debug=None):

        if text is None:
            text = ""

        # if face not in FACES:
        #     raise Exception("Invalid font face: %s" + face)

        self.args = [hjust, vjust, text]
        font = dict(
            family=family,
            weight=face,
            rotation=angle,
            color=color,
            linespacing=lineheight,
            size=size
        )
        font = {k: v for k,v in font.items() if v}
        self.kwargs = dict(horizontalalignment='center', fontdict=font)

    def override(self, *args, **kwargs):
        for key, value in kwargs.items():
            self.kwargs[key] = value
