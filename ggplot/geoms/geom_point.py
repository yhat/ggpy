from .geom import geom
import numpy as np
from ..utils import is_date

class geom_point(geom):
    DEFAULT_AES = {'alpha': 1, 'color': 'black', 'shape': 'o', 'size': 20, 'edgecolors': None}
    REQUIRED_AES = {'x', 'y'}
    _aes_renames = {'size': 's', 'shape': 'marker', 'color': 'c'}

    def plot(self, ax, data, _aes):
        params = self._get_plot_args(data, _aes)
        variables = _aes.data
        x = data[variables['x']]
        y = data[variables['y']]


        if 'colormap' in variables:
            params['cmap'] = variables['colormap']

        if self.params.get("jitter"):
            x *= np.random.uniform(.9, 1.1, len(x))
            y *= np.random.uniform(.9, 1.1, len(y))

        if is_date(x.iloc[0]):
            # TODO: make this work for plot_date params
            ax.plot_date(x, y, **{})
        else:
            print(x, y)
            print(variables)
            ax.scatter(x, y, **params)
