import matplotlib.pyplot as plt
from datasets import diamonds
from matplotlib.patches import Rectangle
from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, DrawingArea, HPacker, VPacker
from collections import defaultdict
import matplotlib.lines as mlines
import numpy as np


def make_shape(color, shape, size, alpha, y_offset = 10, height = 20):
    color = color if color != None else "k" # Default value if None
    shape = shape if shape != None else "o"
    size = size*0.6+45 if size != None else 75
    viz = DrawingArea(30, height, 8, 1)
    key = mlines.Line2D([0], [y_offset], marker=shape, markersize=size/12.0,
                        mec=color, c=color, alpha=alpha)
    viz.add_artist(key)
    return viz

diamonds = diamonds.sample(100)

fig, ax = plt.subplots()
ax.plot(range(5), range(5))

s = make_shape('blue', 'o', 15, 1, y_offset=80)

anchored = AnchoredOffsetbox(loc=4, child=s, pad=0., frameon=False, bbox_to_anchor=(1, 1), bbox_transform=ax.transAxes)
ax.add_artist(s)
# ax.annotate(s, (1, 1), size=15, bbox={'facecolor': 'white'})
plt.show()
