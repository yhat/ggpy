from ggplot import *
import pandas as pd
df = pd.DataFrame(dict(x=range(3), y=range(3), crayon=['sunset orange', 'inchworm', 'cadet blue']))
p = ggplot(aes(x='x', y='y', color='crayon'), data=df)
p += geom_point(size=250)
print(p + scale_color_crayon() + theme_bw())
# print(p + scale_color_crayon())
