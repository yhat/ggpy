# This is dict for documenting ggplot geoms to automatically
# generat docstrings (only parameters) 

# Informations are from matplotlib documentation and from some
# docstrings, which have been already written (e.g in aes.py)

# It's format is in this form:
# "attribute" : ("possible types", "description")
# e.g "x" : ("string, pandas series, list, or numpy array", "x values")

# If better descripton was founded later, the first one is commented out
docs_dict = {
# These are from qplot.py
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
    "linetype" : ("{'solid', 'dashed', 'dashdot', 'dotted'}, optional, default : 'solid'", "set the linestyle"),

#    "linewidth" : ("scalar, default : 1", "Set the linewidth in points"), # replaced by size
    "label" : ("string", "label for the plot"),
    "cmap":("Colormap, optional, default: None", "A Colormap instance or registered name. cmap is only used if color is an array of floats."),

# From ggplot/components/aes.py
    "colour" : ("color of a layer", "Can be continuous or discrete. If continuous, this will be given a color gradient between 2 colors"),

# Shapes can be found on components/shapes.py
    "shape" : ("shape of a point", "Can be used only with geom_point"),

# I think the default value here can be one, since I don't know about
# any other default value than 1
    "size" : ("scalar, default : 1", "Set the linewidth of line or size of point"),

# Specific to only some geoms
    "xmin" : ("float", "min value for a horizonal line"),
    "xmax" : ("float", "max value for a horizonal line"),
    "slope" : ("float (0,1)", "Alope of a line"),
    "intercept" : ("float", "intercept of an abline"),
    "bindwidth" : ("scalar, optional, default: `range/30`", "The relative width of the bars"),

}


### General description of geoms and stats
# Here are simple descriptions of geoms, which we'll be inserted
# to it's geom definition files soon.

# Descriptions from docs.ggplot2.org
# Format:
#    geom/stat_GEOM/STATname
#    short description
#    longer description

"""
geom_abline
Line specified by slope and intercept.
The abline geom adds a line with specified slope and intercept to the plot.

geom_area
Area plot.
An area plot is the continuous analog of a stacked bar chart (see geom_bar), and can be used to show how composition of the whole varies over the range of x. Choosing the order in which different components is stacked is very important, as it becomes increasing hard to see the individual pattern as you move up the stack.

geom_bar
Bars, rectangles with bases on x-axis
The bar geom is used to produce 1d area plots: bar charts for categorical x, and histograms for continuous y. stat_bin explains the details of these summaries in more detail. In particular, you can use the weight aesthetic to create weighted histograms and barcharts where the height of the bar no longer represent a count of observations, but a sum over some other variable. See the examples for a practical example.

geom_density
Display a smooth density estimate.
A smooth density estimate calculated by stat_density.

geom_histogram
Histogram
geom_histogram is an alias for geom_bar plus stat_bin so you will need to look at the documentation for those objects to get more information about the parameters.

geom_hline
Horizontal line.
There are two ways to use it. You can either specify the intercept of the line in the call to the geom, in which case the line will be in the same position in every panel. Alternatively, you can supply a different intercept for each panel using a data.frame. See the examples for the differences

geom_jitter
Points, jittered to reduce overplotting.
The jitter geom is a convenient default for geom_point with position = 'jitter'. See position_jitter to see how to adjust amount of jittering.

geom_line
Connect observations, ordered by x value.
Connect observations, ordered by x value.

geo_now_its_art
There is big bird on it
Plot an awesome bird

geom_point
Points, as for a scatterplot
The point geom is used to create scatterplots.

geom_rect
2d rectangles.
2d rectangles.

geom_step
Connect observations by stairs.
Connect observations by stairs.

geom_text
Textual annotations.
Textual annotations.

geom_tile
Tile plane with rectangles.
Creates a grid of colored or gray-scale rectangles with colors corresponding to the values in z or draws false color level plots and contour plots.

geom_vline
Line, vertical.
This geom allows you to annotate the plot with vertical lines.
"""

# Stats
"""
stat_bin2d
Count number of observation in rectangular bins.
Count number of observation in rectangular bins.

stat_function
Superimpose a function.
Superimpose a function.

stat_smooth
Add a smoother.
Aids the eye in seeing patterns in the presence of overplotting.
"""


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
