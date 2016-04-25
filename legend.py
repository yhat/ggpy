import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def color_legend(color):
    return plt.Line2D([0],[0], color=color, linewidth=5)

def shape_legend(shape):
    return plt.Line2D([0],[0], color='black', marker=shape, linestyle='None')

def linetype_legend(linetype):
    return plt.Line2D([0],[0], color='black', linestyle=linetype)


def make_legend(ax, legend_mapping):
    extra = Rectangle((0, 0), 0, 0, facecolor="w", fill=False, edgecolor='none', linewidth=0)

    items = []
    labels = []

    if 'color' in legend_mapping:
        items.append(extra)
        spacer = '\n' if len(labels) > 0 else ''
        labels.append(spacer + 'color')
        for key, value in legend_mapping['color'].items():
            legend_item = color_legend(value)
            items.append(legend_item)
            labels.append(key)


    if 'shape' in legend_mapping:
        items.append(extra)
        spacer = '\n' if len(labels) > 0 else ''
        labels.append(spacer + 'shape')
        # TODO: for some reason some of these aren't showing up in the legend???
        for key, value in legend_mapping['shape'].items():
            legend_item = shape_legend(value)
            items.append(legend_item)
            labels.append(key)

    if 'linetype' in legend_mapping:
        items.append(extra)
        spacer = '\n' if len(labels) > 0 else ''
        labels.append(spacer + 'linetype')
        for key, value in legend_mapping['linetype'].items():
            legend_item = linetype_legend(value)
            items.append(legend_item)
            labels.append(key)

    ax.legend(items, labels, loc='center left', bbox_to_anchor=(1, 0.5), fontsize='small')
