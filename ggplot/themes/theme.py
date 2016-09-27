from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from copy import deepcopy
import warnings

THEME_PARAMETERS = {
    "axis_line": "?",
    "axis_text": "?",
    "axis_text_x": "?",
    "axis_text_y": "?",
    "axis_title": "?",
    "axis_title_x": "?",
    "axis_title_y": "?",
    "axis_ticks": "?",
    "axis_ticks_length": "?",
    "axis_ticks_margin": "?",
    "legend_background": "?",
    "legend_key": "?",
    "legend_key_size": "?",
    "legend_key_height": "?",
    "legend_key_width": "?",
    "legend_margin": "?",
    "legend_text": "?",
    "legend_text_align": "?",
    "legend_title": "?",
    "legend_title_align": "?",
    "legend_position": "?",
    "legend_direction": "?",
    "legend_justification": "?",
    "legend_box": "?",
    "plot_background": "?",
    "plot_title": "?",
    "plot_margin": "?",
    "strip_background": "?",
    "strip_text_x": "?",
    "strip_text_y": "?",
    "panel_background": "?",
    "panel_border": "?",
    "panel_grid_major_x": "?",
    "panel_grid_minor_x": "?",
    "panel_grid_major_y": "?",
    "panel_grid_minor_y": "?",
    "panel_margin": "?"
}

class theme_base(object):
    _rcParams = {}

    def __init__(self):
        pass

    def __radd__(self, other):
        if other.__class__.__name__=="ggplot":
            other.theme = self
            return other

        return self

    def get_rcParams(self):
        return self._rcParams

    def apply_final_touches(self, ax):
        pass

class theme(theme_base):
    """
    Custom theme for your plot.

    Parameters
    ----------
    title:
        title of your plot
    plot_title:
        title of your plot (same as title)
    plot_margin:
        size of plot margins
    axis_title:
        title of your plot (same as title)
    axis_title_x:
        x axis title
    axis_title_y:
        y axis title
    axis_text:
        theme for text
    axis_text_x:
        theme for x axis text
    axis_text_y:
        theme for y axis text

    Examples
    --------
    >>> ggplot(mtcars, aes(x='mpg')) + geom_histogram() + theme()
    >>> ggplot(mtcars, aes(x='mpg')) + geom_histogram() + theme(plot_margin=dict(bottom=0.2, left=0.2))
    >>> ggplot(mtcars, aes(x='mpg')) + geom_histogram() + theme(axis_text=element_text(size=20))
    >>> ggplot(mtcars, aes(x='mpg')) + geom_histogram() + theme(x_axis_text=element_text(color="orange"), y_axis_text=element_text(color="blue"))
    >>> ggplot(mtcars, aes(x='mpg')) + geom_histogram() + theme(axis_text=element_text(size=20), x_axis_text=element_text(color="orange"), y_axis_text=element_text(color="blue"))
    """
    # this maps theme element names to attributes of a ggplot object. there are
    # more than one way to say the same thing
    ATTRIBUTE_MAPPING = dict(
        # title
        title="title",
        plot_title="title",
        axis_title="title",

        # margins
        plot_margin="margins",

        # text for x and y axis labels
        axis_title_x="xlab",
        axis_title_y="ylab",

        axis_text="axis_text",

        # text for x-axis
        x_axis_text="x_axis_text",
        axis_text_x="x_axis_text",

        # text for y-axis
        y_axis_text="y_axis_text",
        axis_text_y="y_axis_text",
    )
    def __init__(self, *args, **kwargs):
        self.things = deepcopy(kwargs)

    def __radd__(self, other):
        if other.__class__.__name__=="ggplot":
            other.theme = self
            for key, value in self.things.items():
                try:
                    ggplot_attr_name = self.ATTRIBUTE_MAPPING[key]
                except:
                    msg = "%s is an invalid theme parameter" % key
                    warnings.warn(msg, RuntimeWarning)
                    continue
                setattr(other, ggplot_attr_name, value)
            return other

        return self

    def parameter_lookup(self, parameter):
        return THEME_PARAMETERS.get(parameter)
