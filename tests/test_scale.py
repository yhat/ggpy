from ggplot import *
import pandas as pd

df = pd.DataFrame(dict(x=range(3), y=range(3), crayon=['sunset orange', 'inchworm', 'cadet blue']))
p = ggplot(aes(x='x', y='y', color='crayon'), data=df)
p += geom_point(size=250)
print(p + scale_color_crayon() + theme_bw())

p = ggplot(aes(x='x', fill='crayon'), data=df) + geom_bar()
print p + scale_fill_brewer(type='qual')

p = ggplot(aes(x='x', fill='crayon'), data=df) + geom_bar()
print p + scale_fill_crayon()

p = ggplot(aes(x='x', fill='crayon'), data=df) + geom_bar()
print p + scale_fill_manual(values=['green', 'purple', 'turquoise'])
