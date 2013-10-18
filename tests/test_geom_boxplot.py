# Tests for geom_boxplot

from ggplot import *

p = ggplot(mtcars, aes('factor(cyl)',y='mpg'))
p + geom_bar()
