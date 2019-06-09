from __future__ import print_function
from ggplot import *

meat = meat.set_index(['date'])

print(ggplot(meat, aes(x='__index__', y='beef')) + geom_point())
