from .geom import geom
from ..utils import is_date


class geom_text(geom):
    DEFAULT_AES = {'alpha': 1, 'rotation': 0, 'color': 'black', 'size': 12}
    REQUIRED_AES = {'x', 'y', 'label'}
    _aes_renames = {'size': 'fontsize'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
        x = data[variables['x']]
        y = data[variables['y']]
        labels = data[variables['label']]

        params = self._get_plot_args(data, _aes)

        if 'colormap' in variables:
            params['cmap'] = variables['colormap']

        if self.params.get("jitter"):
            x *= np.random.uniform(.9, 1.1, len(x))
            y *= np.random.uniform(.9, 1.1, len(y))

        if is_date(x.iloc[0]):
            raise Exception("Can't do geom_text with a x-axis that is a date")
        else:
            ax.plot(x, y)
            for (xi, yi, li) in zip(x, y, labels):
                xi += self.params.get('hjust', 0.)
                yi += self.params.get('vjust', 0.)
                ax.text(xi, yi, li, **params)
            ax.autoscale_view()
