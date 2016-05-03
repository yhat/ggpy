import seaborn as sns
import itertools

SHAPES = [
    'o',#circle
    '^',#triangle up
    'D',#diamond
    'v',#triangle down
    # '+',#plus # doesn't render in legend for some reason
    # 'x',#x # also doesn't render in legend for some reason
    's',#square
    '*',#star
    'p',#pentagon
    '8',#octagon
    "_",#hline
    "|",#vline
    "_",#hline
]


def shape_gen():
    while True:
        for shape in SHAPES:
            yield shape

def size_gen(uniq_values):
    n = len(uniq_values)
    low = 10
    for i in range(low, low + n*10, 10):
        yield i

def color_gen(colors=None):
    if colors:
        pal = colors
    else:
        pal = sns.color_palette()
    generator = itertools.cycle(pal)
    while True:
        yield next(generator)

# Matplolib is not consistent. Sometimes it does not
# accept abbreviations
# LINETYPES = [
#     '-',  #solid
#     '--', #dashed
#     '-.', #dash-dot
#     ':',  #dotted
#     '.',  #point
#     '|',  #vline
#     '_',  #hline
# ]

LINETYPES = [
    'solid',
    'dashed',
    'dashdot',
    'dotted'
]

def linetype_gen():
    while True:
        for line in LINETYPES:
            yield line
