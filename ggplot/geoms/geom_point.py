from .geom import geom
import numpy as np
import pandas as pd
import datetime

class geom_point(geom):
    DEFAULT_AES = {'alpha': 1, 'color': 'black', 'shape': 'o', 'size': 20, 'edgecolors': None}
    REQUIRED_AES = {'x', 'y'}
    _aes_renames = {'size': 's', 'shape': 'marker', 'color': 'c'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
        x = data[variables['x']]
        y = data[variables['y']]

        params = self._get_plot_args(data, _aes)

        if 'colormap' in variables:
            params['cmap'] = variables['colormap']

        if self.params.get("jitter"):
            x *= np.random.uniform(.9, 1.1, len(x))
            y *= np.random.uniform(.9, 1.1, len(y))

        date_types = (
            pd.tslib.Timestamp,
            pd.DatetimeIndex,
            pd.Period,
            pd.PeriodIndex,
            datetime.datetime,
            datetime.time
        )
        if isinstance(x.iloc[0], date_types):
            # TODO: make this work for plot_date params
            ax.plot_date(x, y, **{})
        else:
            ax.scatter(x, y, **params)
