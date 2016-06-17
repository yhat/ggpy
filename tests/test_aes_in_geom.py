from ggplot import *


print ggplot(mtcars, aes(x='wt', y='mpg')) + geom_point(aes(size='cyl'), color='blue')
