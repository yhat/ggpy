from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from matplotlib.text import Text

FACES = ["plain", "italic", "bold", "bold.italic"]

class element_text(object):
    """
    Customize text for your plots

    Parameters
    ----------
    text:
        value of text
    family:
        font family
    face:
        ????
    color:
        color of the text
    size:
        font size
    hjust:
        horizontal adjustment from true x
    vjust:
        vertical adjustment from true y
    angle:
        rotate text
    lineheight:
        spacing between lines of text
    margin:
        margin around text

    Examples
    --------
    >>> theme(axis_text=element_text(size=20))
    >>> theme(x_axis_text=element_text(color="orange"), y_axis_text=element_text(color="blue"))
    >>> theme(axis_text=element_text(size=20), x_axis_text=element_text(color="orange"), y_axis_text=element_text(color="blue"))
    """
    def __init__(self, text=None, family=None, face=None, color=None, size=None,
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

    def override(self, x, y, overrides={}):
        self.args[0] += x
        self.args[1] += y
        for key, value in overrides.items():
            self.kwargs[key] = value

    def apply_to_fig(self, fig):
        fig.text(*self.args, **self.kwargs)
