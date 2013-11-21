# Tests for geom_boxplot

from ggplot import *
from pandas import DataFrame
import numpy as np

df = DataFrame(np.random.rand(15,1)*10,columns=["X"])


p = ggplot(df, aes(x='X')) 
print p + geom_boxplot()
print df.boxplot()
plt.show(1)

