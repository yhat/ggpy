from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import pandas as pd
import os

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
