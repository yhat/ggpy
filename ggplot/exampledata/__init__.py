import os
import sys

# These data sets need implicit imports anyway as __ALL__ does not work because of the 
# workaround for not loading the data sets on import. So make that at 
# least clear when you poke around...
__ALL__ = []

# Workaround for lazy loading the data sets on first useage and NOT on imprting them
# http://stackoverflow.com/questions/880530/can-python-modules-have-properties-the-same-way-that-objects-can
class _Datasets(object):
    __ALL__ = []
    _ROOT = os.path.abspath(os.path.dirname(__file__))
    _DATA = {}
    def _getter_proxy(name):
        def wrapped_getter(self):
            if not name in self._DATA:
                import pandas as pd
                import os
                self._DATA[name] = pd.read_csv(os.path.join(self._ROOT, name))
            return self._DATA[name]
        return wrapped_getter

    diamonds = property(_getter_proxy("diamonds.csv"), None, None, "Prices of 50,000 round cut diamonds")
    mtcars = property(_getter_proxy("mtcars.csv"), None, None, "Fuel consumption and 10 aspects of automobile design and performance for 32 automobiles (1973-74 models)")
    meat = property(_getter_proxy("meat.csv"), None, None, "Livestock and Meat Domestic Data (1944-2012)")
    pageviews = property(_getter_proxy("pageviews.csv"), None, None, "Page view data (2012-2013)")

# replace the module with the object 
sys.modules[__name__] = _Datasets()
    
