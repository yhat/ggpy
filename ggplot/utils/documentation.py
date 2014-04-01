# Here lies dict for documenting ggplot geoms to use automatically
# generated help docstrings (only parameters) 

# Informations were taken from matplotlib documentation and from some
# docstrings, which have been already written (e.g aes.py)

# It's format is in this form:
# "attribut" : ("possible types", "description")
# e.g "x" : ("string, pandas series, list, or numpy array", "x values")

# If better descripton was founded later, the first one is uncommented
docs_dict = {
    "x": ("string, pandas series, list, or numpy array", "x values"),
    "y": ("string, pandas series, list, or numpy array", "y values"),
#    "color": ("string", "color values"),
#    "size": ("string", "size values"),
    "fill": ("string", "fill values"),
    "data": ("data frame", "data frame to use for the plot"),
    "geom": ("string (geom)", "string that specifies which type of plot to make"),
    "stat": ("list", "specifies which statistics to use"),
    "position": ("list", "gives position adjustment to use"),
    "xlim": ("tuple", "limits on x axis; i.e. (0, 10)"),
    "ylim": ("tuple, None", "limits on y axis; i.e. (0, 10)"),
    "log": ('{"x", "y", "xy"}', 'which variables to log transform'),
    "main": ("string", "title for the plot"),
    "xlab": ("string", "title for the x axis"),
    "ylab": ("string", "title for the y axis"),
    "asp": ("string", "the y/x aspect ratio"),

# Not from qplot.py
    "alpha" : ("scalar, optional", "The alpha blending value, between 0 and 1. Only supported for hard coded values"),
# Linestyles can be found in components/linestyles.py
    "linestyle" : ("{'solid', 'dashed', 'dashdot', 'dotted'}, optional, default : 'solid'", "set the linestyle"),
    "linewidth" : ("scalar, default : 1", "Set the linewidth in points"),
    "label" : ("string", "label for the plot"),
    "cmap":("Colormap, optional, default: None", "A Colormap instance or registered name. cmap is only used if color is an array of floats."),

# From ggplot/components/aes.py
    "color" : ("color of a layer", "Can be continuous or discrete. If continuous, this will be given a color gradient between 2 colors"),
# Shapes can be found on components/shapes.py
    "shape" : ("shape of a point", "Can be used only with geom_point"),
    "size" : ("size of a point or line", "Used to give a relative size for a continuous value"),

# Specific to only some geoms
    "xmin" : ("float", "min value for a horizonal line"),
    "xmax" : ("float", "max value for a horizonal line"),
    "slope" : ("float (0,1)", "Alope of a line"),
    "intercept" : ("float", "intercept of an abline"),
    "bindwidth" : ("scalar, optional, default: `range/30`", "The relative width of the bars"),

}

### Problems ###
# There is problem with adding default values (they vary somewhere), e.g
# geom_rect has default 'color': '#333333 and geom_abline 'color': 'black

# Some of the parameters can be required in some geom but are optional
# for others. Numpy documentation standard doesn't notice adding 
# bold font to required parameters

### TODO ###
# Missing docs
# "group" : ("","")


## stat_*.py 
# These are not well documented yet in current stat_* functions
#    "method" : 
#    "se" : 
#    "span" :
#    "level" :
#    "window" : 
#    "fun" : 
#    "n" :
#    "args" : 
