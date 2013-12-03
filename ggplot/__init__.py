# For testing purposes we might need to set mpl backend before any
# other import of matplotlib.
def _set_mpl_backend():
    import os
    import matplotlib as mpl

    env_backend = os.environ.get('MATPLOTLIB_BACKEND')
    if env_backend:
        # we were instructed
        mpl.use(env_backend)

_set_mpl_backend()

from .ggplot import *

# Needs implicit imports as __ALL__ does not work because of the 
# workaround for not loading the data sets on import.
from .exampledata import diamonds,mtcars,meat,pageviews
