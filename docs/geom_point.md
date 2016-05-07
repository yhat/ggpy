# geom_point


```python
ggplot(mtcars, aes(x='wt', y='mpg')) + geom_point()
```

```python
ggplot(mtcars, aes(x='wt', y='mpg', color='cyl')) + geom_point()
```

```python
ggplot(mtcars, aes(x='wt', y='mpg', shape='cyl')) + geom_point()
```

```python
ggplot(diamonds, aes(x='carat', y='price')) + geom_point()
```

```python
ggplot(diamonds, aes(x='carat', y='price')) + geom_point(color='steelblue')
```

```python
ggplot(diamonds, aes(x='carat', y='price')) + geom_point(alpha=1/100.)
```
