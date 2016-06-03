# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ggplot import *

print ggplot(mtcars, aes(x='mpg')) + geom_histogram() + xlab("Scrüm")
