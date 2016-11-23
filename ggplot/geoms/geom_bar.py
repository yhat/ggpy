from collections import OrderedDict
from .geom import geom
import pandas as pd
import matplotlib.patches as patches


class geom_bar(geom):
    """
    Bar chart

    Parameters
    ----------
    x:
        x values for bins/categories
    color:
        color of the outer line
    alpha:
        transparency of fill
    size:
        thickness of outer line
    linetype:
        type of the outer line ('solid', 'dashed', 'dashdot', 'dotted')
    fill:
        color the interior of the bar will be

    Examples
    --------
    """

    DEFAULT_AES = {'alpha': None, 'color': None, 'fill': '#333333',
                   'linetype': 'solid', 'size': 1.0}
    REQUIRED_AES = {'x'}
    DEFAULT_PARAMS = {"width": 0.8}
    _aes_renames = OrderedDict([
        ('linetype', 'linestyle'),
        ('size', 'linewidth'),
        ('color', 'edgecolor'), # Before fill -> color
        ('fill', 'color'),
    ])

    def setup_data(self, data, _aes, facets=None):
        (data, _aes) = self._update_data(data, _aes)
        x_col = _aes['x']
        weight_col = _aes.get('weight')

        if not weight_col:
            if '__weight__' not in data:
                data.insert(0, '__weight__', 1)
            weight_col = '__weight__'
        else:
            data['__weight__'] = data[weight_col]
            weight_col = '__weight__'

        fill_col = _aes.get('fill')
        if fill_col:
            fill_col = [fill_col]
        else:
            fill_col = []

        groupers = [x_col]
        if facets:
            if facets.rowvar:
                groupers.append(facets.rowvar)
            if facets.colvar:
                groupers.append(facets.colvar)
        dfa = (data[groupers + fill_col + [weight_col]].groupby(groupers + fill_col).sum()).reset_index()
        dfb = (data[groupers + [weight_col]].groupby(groupers).sum()).reset_index()
        df = pd.merge(dfa, dfb, on=groupers)
        df.rename(columns={'__weight___x': '__weight__', '__weight___y': '__total_weight__'}, inplace=True)
        if self.params.get('position')=='fill':
            df['__calc_weight__'] = df['__weight__'] / df['__total_weight__']
        else:
            df['__calc_weight__'] = df['__weight__']
        return df


    def plot(self, ax, data, _aes, x_levels, fill_levels, lookups):
        (data, _aes) = self._update_data(data, _aes)
        variables = _aes.data
        weight_col = _aes.get('weight')
        x_levels = sorted(x_levels)

        if not weight_col:
            if '__weight__' not in data:
                data.insert(0, '__weight__', 1.0)
            weight_col = '__weight__'

        params = self._get_plot_args(data, _aes)

        if fill_levels is not None:
            width = self.params["width"] / len(fill_levels)
        else:
            width = self.params["width"]
        padding = width / 2


        xticks = []
        for i, x_level in enumerate(x_levels):
            mask = data[variables['x']]==x_level
            row = data[mask]
            if len(row)==0:
                xticks.append(i)
                continue

            if fill_levels is not None:
                fillval = row[variables['fill']].iloc[0]
                fill_idx = fill_levels.tolist().index(fillval)
                fill_x_adjustment = width * len(fill_levels)/2.
            else:
                fill_x_adjustment = width / 2

            if self.params.get('position') in ('stack', 'fill'):
                dodge = 0.0
                fill_x_adjustment = width / 2
                if fill_levels is None:
                    height = 1.0
                    ypos = 0
                else:
                    mask = (lookups[variables['x']]==x_level) & (lookups[variables['fill']]==fillval)
                    height = lookups[mask]['__calc_weight__'].sum()
                    mask = (lookups[variables['x']]==x_level) & (lookups[variables['fill']] < fillval)
                    ypos = lookups[mask]['__calc_weight__'].sum()
            else:
                if fill_levels is not None:
                    dodge = (width * fill_idx)
                else:
                    dodge = width
                ypos = 0.0
                height = row[weight_col].sum()

            xy = (dodge + i  - fill_x_adjustment, ypos)

            ax.add_patch(patches.Rectangle(xy, width, height, **params))
            if fill_levels is not None:
                xticks.append(i)
            else:
                xticks.append(i + dodge)

        # need this b/c we're using patches
        ax.autoscale_view()

        # this will happen multiple times, but it's ok b/c it'll be the same each time
        ax.set_xticks(xticks)
        ax.set_xticklabels(x_levels)
