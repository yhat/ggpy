from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from .geom import geom
from pandas.lib import Timestamp
from ggplot.components.colors import color_gen

class geom_bar(geom):
    VALID_AES = ['x', 'color', 'alpha', 'fill', 'label', 'weight', 'position']

    def plot_layer(self, layer):
        layer = dict((k, v) for k, v in layer.items() if k in self.VALID_AES)
        layer.update(self.manual_aes)

        x = layer.pop('x')
        if 'weight' not in layer:
            counts = pd.value_counts(x)
            labels = counts.index.tolist()
            weights = counts.tolist()
        else:
            # TODO: pretty sure this isn't right
            weights = layer.pop('weight')
            if not isinstance(x[0], Timestamp):
                labels = x
            else:
                df = pd.DataFrame({'weights':weights, 'timepoint': pd.to_datetime(x)})
                df = df.set_index('timepoint')
                ts = pd.TimeSeries(df.weights, index=df.index)
                ts = ts.resample('W', how='sum')
                ts = ts.fillna(0)
                weights = ts.values.tolist()
                labels = ts.index.to_pydatetime().tolist()

        indentation = np.arange(len(labels)) + 0.2
        width = 0.9
        idx = np.argsort(labels)
        labels, weights = np.array(labels)[idx], np.array(weights)[idx]
        labels = sorted(labels)

        if 'color' in layer:
            layer['edgecolor'] = layer['color']
            del layer['color']
        else:
            layer['edgecolor'] = '#333333'

        if 'fill' in layer:
            fill = layer.pop('fill')
            if type(fill) is list:
                position = layer.get('position','stacked')
                fill_labels = np.unique(fill).tolist()
                bottom = np.zeros(len(labels),dtype=np.int)
                color_cycle = color_gen(len(fill_labels))
                for i,fill_label in enumerate(fill_labels):
                    color = color_cycle.next()
                    fill_x = np.array(x)[np.array(fill) == np.array(fill_label)]
                    counts = pd.value_counts(fill_x)
                    weights = counts.reindex(labels,fill_value=0).tolist()
                    if position == 'dodge':
                        bar_width = width / len(fill_labels)
                        plt.bar(indentation+(bar_width * i),
                                weights,
                                bar_width,
                                color=color,
                                label=fill_label)
                    else:
                        plt.bar(indentation,
                                weights,
                                width,
                                color=color,
                                bottom=bottom,
                                label=fill_label)
                        bottom += weights
                    plt.autoscale()
                return [
                    {"function": "set_xticks", "args": [indentation+width/2]},
                    {"function": "set_xticklabels", "args": [labels]},
                    {"function": "set_ylabel", "args": ["count"]},
                    {"function": "legend","args":[]},
                ]
            else:
                layer['color'] = fill
        else:
            layer['color'] = '#333333'

        plt.bar(indentation, weights, width, **layer)
        plt.autoscale()
        return [
                {"function": "set_xticks", "args": [indentation+width/2]},
                {"function": "set_xticklabels", "args": [labels]},
                {"function": "set_ylabel", "args": ["count"]},
            ]
