from .geom_point import geom_point


class geom_jitter(geom_point):
    """
    Same as geom_point but with randomness added so you can see the points better

    y:
        ...description...
    x:
        ...description...
    color:
        ...description...
    alpha:
        ...description...
    shape:
        ...description...
    edgecolors:
        ...description...
    size:
        ...description...

    Examples
    --------
    """
    def __init__(self, *args, **kwargs):
        super(geom_point, self).__init__(*args, **kwargs)
        self.params['position'] = "jitter"
