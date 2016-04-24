import seaborn as sns
import itertools

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

def palette_gen(colors=None):
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
