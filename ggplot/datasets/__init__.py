from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import pandas as pd
import os
import sys

_ROOT = os.path.abspath(os.path.dirname(__file__))

diamonds = pd.read_csv(os.path.join(_ROOT, "diamonds.csv"))
mtcars = pd.read_csv(os.path.join(_ROOT, "mtcars.csv"))
meat = pd.read_csv(os.path.join(_ROOT, "meat.csv"), parse_dates=[0])
movies = pd.read_csv(os.path.join(_ROOT, "movies.csv"))
pageviews = pd.read_csv(os.path.join(_ROOT, "pageviews.csv"), parse_dates=[0])
pigeons = pd.read_csv(os.path.join(_ROOT, "pigeons.csv"))
chopsticks = pd.read_csv(os.path.join(_ROOT, "chopsticks.csv"))
mpg = pd.read_csv(os.path.join(_ROOT, "mpg.csv"))
salmon = pd.read_csv(os.path.join(_ROOT, "salmon.csv"))

def load_world():
    """
    Load world map data. This will return a data frame that contains
    countries and their coordinate boundaries.

    Examples
    --------
    >>> load_world().head()
      country        lat        lng  part country-part    lat_proj    lng_proj
    0   Aruba  12.577582 -69.996938     0       Aruba0  206.255742  232.225312
    1   Aruba  12.531724 -69.936391     0       Aruba0  206.369267  232.313402
    2   Aruba  12.519232 -69.924672     0       Aruba0  206.391240  232.337395
    3   Aruba  12.497016 -69.915761     0       Aruba0  206.407948  232.380064
    4   Aruba  12.453559 -69.880198     0       Aruba0  206.474629  232.463517
    >>> load_world().tail()
             country        lat        lng  part country-part    lat_proj  \
    548651  Zimbabwe -15.619666  29.814283     0    Zimbabwe0  393.401781
    548652  Zimbabwe -15.614808  29.837331     0    Zimbabwe0  393.444995
    548653  Zimbabwe -15.618839  29.881773     0    Zimbabwe0  393.528323
    548654  Zimbabwe -15.641473  29.967504     0    Zimbabwe0  393.689069
    548655  Zimbabwe -15.646227  30.010654     0    Zimbabwe0  393.769975

              lng_proj
    548651  285.656522
    548652  285.647065
    548653  285.654913
    548654  285.698982
    548655  285.708239
    """
    _DATA_DIR = os.path.join(os.path.expanduser("~"), ".ggplot")
    if not os.path.exists(_DATA_DIR):
        os.mkdir(_DATA_DIR)

    f = os.path.join(_DATA_DIR, "world.csv")
    if os.path.exists(f):
        world = pd.read_csv(f)
    else:
        sys.stderr.write("downloading world data set...")
        url = "https://raw.githubusercontent.com/yhat/ggplot/master/data/world.csv"
        world = pd.read_csv(url)
        world.to_csv(f, index=False)
        sys.stderr.write("done!")
    return world
