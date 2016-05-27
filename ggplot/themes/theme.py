from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

class theme_base(object):
    def __init__(self):
        self._rcParams = {}

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
    def __init__(self, *args, **kwargs):
        pass
