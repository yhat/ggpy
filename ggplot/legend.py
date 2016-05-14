from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import re

def tex_escape(text):
    """
        :param text: a plain text message
        :return: the message escaped to appear correctly in LaTeX
    """
    conv = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
        '<': r'\textless',
        '>': r'\textgreater',
    }
    regex = re.compile('|'.join(re.escape(unicode(key)) for key in sorted(conv.keys(), key = lambda item: - len(item))))
    return regex.sub(lambda match: conv[match.group()], text)

def color_legend(color):
    # TODO: need outline on line
    return plt.Line2D([0],[0], color=color, linewidth=5)

# TODO(bug): this *sometimes* decides to not use marker='o'
def size_legend(size):
    return plt.Line2D([0],[0], color='black', marker='o', linestyle='None', markersize=size**.5)

def alpha_legend(alpha):
    return plt.Line2D([0],[0], color='black', marker='o', linestyle='None', alpha=alpha)

def shape_legend(shape):
    return plt.Line2D([0],[0], color='black', marker=shape, linestyle='None')

def linetype_legend(linetype):
    return plt.Line2D([0],[0], color='black', linestyle=linetype)


def make_legend(ax, legend_mapping):
    # TODO: for some reason this reaks havoc! but this is also how you would do a bold legend :(
    # plt.rc('text', usetex=True)

    extra = Rectangle((0, 0), 0, 0, facecolor="w", fill=False, edgecolor='none', linewidth=0)

    items = []
    labels = []

    if 'color' in legend_mapping:
        items.append(extra)
        colname = legend_mapping['color']['name']
        # spacer = r'\n' if len(labels) > 0 else r''
        spacer = '\n' if len(labels) > 0 else ''
        # TODO: this is supposed to make the label bold
        # labels.append(spacer + r'\textbf{' + colname + '}')
        labels.append(spacer + colname)
        for key in sorted(legend_mapping['color']['lookup'].keys()):
            value = legend_mapping['color']['lookup'][key]
            legend_item = color_legend(value)
            items.append(legend_item)
            labels.append(key)

    if 'fill' in legend_mapping:
        items.append(extra)
        colname = legend_mapping['fill']['name']
        # spacer = r'\n' if len(labels) > 0 else r''
        spacer = '\n' if len(labels) > 0 else ''
        # TODO: this is supposed to make the label bold
        # labels.append(spacer + r'\textbf{' + colname + '}')
        labels.append(spacer + colname)
        for key in sorted(legend_mapping['fill']['lookup'].keys()):
            value = legend_mapping['fill']['lookup'][key]
            legend_item = color_legend(value)
            items.append(legend_item)
            labels.append(key)

    if 'shape' in legend_mapping:
        items.append(extra)
        colname = legend_mapping['shape']['name']
        # spacer = r'\n' if len(labels) > 0 else r''
        spacer = '\n' if len(labels) > 0 else ''
        # TODO: this is supposed to make the label bold
        # labels.append(spacer + r'\textbf{' + colname + '}')
        labels.append(spacer + colname)
        for key in sorted(legend_mapping['shape']['lookup'].keys()):
            value = legend_mapping['shape']['lookup'][key]
            legend_item = shape_legend(value)
            items.append(legend_item)
            labels.append(key)

    if 'alpha' in legend_mapping:
        items.append(extra)
        colname = legend_mapping['alpha']['name']
        # spacer = r'\n' if len(labels) > 0 else r''
        spacer = '\n' if len(labels) > 0 else ''
        # TODO: this is supposed to make the label bold
        # labels.append(spacer + r'\textbf{' + colname + '}')
        labels.append(spacer + colname)
        for key in sorted(legend_mapping['alpha']['lookup'].keys()):
            value = legend_mapping['alpha']['lookup'][key]
            legend_item = alpha_legend(value)
            items.append(legend_item)
            labels.append(key)

    if 'size' in legend_mapping:
        items.append(extra)
        colname = legend_mapping['size']['name']
        # spacer = r'\n' if len(labels) > 0 else r''
        spacer = '\n' if len(labels) > 0 else ''
        # TODO: this is supposed to make the label bold
        # labels.append(spacer + r'\textbf{' + colname + '}')
        labels.append(spacer + colname)
        for key in sorted(legend_mapping['size']['lookup'].keys()):
            value = legend_mapping['size']['lookup'][key]
            legend_item = size_legend(value)
            items.append(legend_item)
            labels.append(key)

    if 'linetype' in legend_mapping:
        items.append(extra)
        colname = legend_mapping['linetype']['name']
        # spacer = r'\n' if len(labels) > 0 else r''
        spacer = '\n' if len(labels) > 0 else ''
        # TODO: this is supposed to make the label bold
        # labels.append(spacer + r'\textbf{' + colname + '}')
        labels.append(spacer + colname)
        for key in sorted(legend_mapping['linetype']['lookup'].keys()):
            value = legend_mapping['linetype']['lookup'][key]
            legend_item = linetype_legend(value)
            items.append(legend_item)
            labels.append(key)

    legend = ax.legend(items, labels, loc='center left', bbox_to_anchor=(1.05, 0.5), fontsize='small', frameon=False)
