from ggplot import *


print ggplot(mpg, aes(x='class', y='hwy')) + geom_errorbar()
