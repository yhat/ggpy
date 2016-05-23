from .geom import geom
import matplotlib.pyplot as plt

class geom_boxplot(geom):
    DEFAULT_AES = {'y': None, 'color': 'black', 'flier_marker': '+'}
    REQUIRED_AES = {'x'}
    DEFAULT_PARAMS = {'stat': 'identity', 'position': 'identity'}

    def plot(self, ax, data, _aes):
        variables = _aes.data
        x = data[variables['x']]
        params = self._get_plot_args(data, _aes)

        q = ax.boxplot(x, vert=True)
        plt.setp(q['boxes'], color=params['color'])
        plt.setp(q['whiskers'], color=params['color'])
        plt.setp(q['fliers'], color=params['color'])
