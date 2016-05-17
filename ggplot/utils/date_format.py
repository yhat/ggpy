from matplotlib.dates import DateFormatter

def date_format(format='%Y-%m-%d',tz=None):
    """
    "Formatted dates."

    Arguments:
        format => Date format using standard strftime format.
        tz => Instance of datetime.tzinfo

    Example:
        date_format('%b-%y')
        date_format('%B %d, %Y')
    """
    return DateFormatter(format,tz)
