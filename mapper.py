import seaborn as sns
import pandas as pd
from matplotlib.colors import rgb2hex
import matplotlib.pyplot as plt
import itertools


aes = {
    'x': 'total_bill',
    'y': 'tip',
    'color': 'sex',
    'shape': 'smoker'
}

tips = sns.load_dataset('tips')

print aes
palette = itertools.cycle(sns.color_palette())

color_map = {}
for item in tips[aes['color']].unique():
    color_map[item] = rgb2hex(next(palette))
print color_map

tips[aes['color']] = tips[aes['color']].apply(lambda x: color_map[x])

SHAPES = [
    'o',#circle
    '^',#triangle up
    'D',#diamond
    'v',#triangle down
    '+',#plus
    'x',#x
    's',#square
    '*',#star
    'p',#pentagon
    '*'#octagon
]

def shape_gen():
    while True:
        for shape in SHAPES:
            yield shape

shapes = shape_gen()
shape_map = {}
for item in tips[aes['shape']].unique():
    shape_map[item] = next(shapes)
print shape_map

tips[aes['shape']] = tips[aes['shape']].apply(lambda x: shape_map[x])

discrete = [aes[k] for k in ['color', 'shape']]
for _, seg in tips.groupby(discrete):
    plt.scatter(seg[aes['x']], seg[aes['y']], c=seg[aes['color']].iloc[0] , marker=seg[aes['shape']].iloc[0])
plt.show()
