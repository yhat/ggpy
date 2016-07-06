from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from copy import deepcopy

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
    # this maps theme element names to attributes of a ggplot object
    ATTRIBUTE_MAPPING = dict(
        title="title",
        plot_title="title",
        plot_margin="margins",
        axis_title="title",
        axis_title_x="xlab",
        axis_title_y="ylab",
        axis_text="axis_text",
        axis_text_x="x_axis_text",
        axis_text_y="y_axis_text",
    )
    def __init__(self, *args, **kwargs):
        self.things = deepcopy(kwargs)

    def __radd__(self, other):
        if other.__class__.__name__=="ggplot":
            other.theme = self
            for key, value in self.things.items():
                key = self.ATTRIBUTE_MAPPING.get(key, key)
                setattr(other, key, value)
            return other

        return self

    def parameter_lookup(self, parameter):
        return THEME_PARAMETERS.get(parameter)
