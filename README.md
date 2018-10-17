# ggplot - a working, maintained fork

## Why this fork?
`ggplot` is a great python library. However, it is no longer maintained by its owner and still has a bunch of issues which remain unsolved. Some of these include incompatibility with newer versions of `pandas` and Python 3.

Many projects still rely on `ggplot` and many have to either move to alternatives or manually update `ggpy`'s code after installing it  to fix compatibility issues. To get a better context of the issue you can refer to [#654 Is this project dead?](https://github.com/yhat/ggpy/issues/654)

This fork is a working copy of `ggplot` which is readily maintained and is open to updates and fixes so that developers do not have to make fixes manually.

## Installation
```bash
$ pip3 install git+https://github.com/sushinoya/ggpy
```

## What is ggpy?
`ggplot` is a Python implementation of the grammar of graphics. It is not intended
to be a feature-for-feature port of [`ggplot2 for R`](https://github.com/hadley/ggplot2)--though 
there is much greatness in `ggplot2`, the Python world could stand to benefit 
from it. So there __will be feature overlap__, but not neccessarily mimicry 
(after all, R is a little weird).

You can do cool things like this:

```python
ggplot(diamonds, aes(x='price', color='clarity')) + \
    geom_density() + \
    scale_color_brewer(type='div', palette=7) + \
    facet_wrap('cut')
```
![](./docs/example.png)
