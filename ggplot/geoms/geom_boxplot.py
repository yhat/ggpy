import matplotlib.pyplot as plt
import numpy as np
from .geom import geom

class geom_boxplot(geom):
    VALID_AES = ['lower','middle','upper','x','ymax','ymin','alpha',
                 'colour','color','fill','linetype','shape','size','weight']


    def plot_layer(self, layer):
        layer = {k: v for k, v in layer.items() if k in self.VALID_AES}
        layer.update(self.manual_aes)
        
        # Boxplot does not like ints in the numpy array
        # Change it to float32
        if "x" in layer:
            layer["x"] = np.float32(layer["x"])        
            
        plt.boxplot(**layer)

