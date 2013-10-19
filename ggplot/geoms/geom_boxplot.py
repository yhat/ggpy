import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from pandas import DataFrame
import numpy as np
from .geom import geom

class geom_boxplot(geom):
    VALID_AES = ['lower','middle','upper','x','ymax','ymin','alpha',
                 'colour','color','fill','linetype','shape','size','weight']


    def plot_layer(self, layer):
        layer = {k: v for k, v in layer.items() if k in self.VALID_AES}
        layer.update(self.manual_aes)
            
        # Option 1 (No Pandas)
            
        # Boxplot takes in an array or sequence of vectors
        # The goal is to group the 'y' values by grouped 'x'
        # Then take the transpose and give it to plt.boxplot(**layer)
        # If we do not have a y value, no need to change anything
        #        if "y" in layer:
        # list(set([...])) just gets unique elements
        #           unique = list(set(layer["x"]))            
        # Group y values in len(x) arrays, having values y.x
        # Store it back in x as a transpose.            
        #          pass
  
        # plt.boxplot(**layer)
        # Option 2 With Pandas and DataFrame.boxplot()
        # Need access to the DataFrame passed to ggplot(..)
        df = DataFrame(layer["x"])    
        df.boxplot()

