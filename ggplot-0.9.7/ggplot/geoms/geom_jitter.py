from .geom_point import geom_point


class geom_jitter(geom_point):
    def __init__(self, *args, **kwargs):
        super(geom_point, self).__init__(*args, **kwargs)
        self.params['position'] = "jitter"
