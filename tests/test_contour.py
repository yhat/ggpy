import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.random.uniform(-1, 1, 100)
y = np.random.uniform(-1, 1, 100)
z = np.random.uniform(-1, 1, 100)


df = pd.DataFrame(dict(x=x, y=y, z=z))

f, ax = plt.subplots()

# ax.contourf(x, y, z, 1000, cmap=plt.cm.Blues)
# ax.hist2d(x, y)

f.savefig('/tmp/stuff.png')
