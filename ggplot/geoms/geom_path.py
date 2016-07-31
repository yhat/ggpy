from .geom_line import geom_line


class geom_path(geom_line):
    """
    Sequence of connected (x, y) coordinates

    Parameters
    ----------
    x:
        x values for (x, y) coordinates
    y:
        y values for (x, y) coordinates
    color:
        color of line
    alpha:
        transparency of color
    linetype:
        type of the line ('solid', 'dashed', 'dashdot', 'dotted')
    size:
        thickness of line

    Examples
    --------
    """
    is_path = True
