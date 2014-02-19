from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from ggplot import *
# the following should not raise exceptions.
[i for i,_ in zip(components.colors.color_gen(10),range(5))]
print(ggplot(mtcars, aes("qsec", "wt", colour = 'name')) + geom_point())
