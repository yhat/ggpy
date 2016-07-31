from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from matplotlib.dates import DateFormatter
from matplotlib.dates import MinuteLocator, HourLocator, DayLocator
from matplotlib.dates import WeekdayLocator, MonthLocator, YearLocator

def date_format(format='%Y-%m-%d', tz=None):
    """
    Format dates

    Parameters
    ----------
    format:
        Date format using standard strftime format.
    tz:
        Instance of datetime.tzinfo

    Examples
    --------
    >>> date_format('%b-%y')
    >>> date_format('%B %d, %Y')
    """
    return DateFormatter(format, tz)

def parse_break_str(txt):
    "parses '10 weeks' into tuple (10, week)."
    txt = txt.strip()
    if len(txt.split()) == 2:
        n, units = txt.split()
    else:
        n,units = 1, txt
    units = units.rstrip('s') # e.g. weeks => week
    n = int(n)
    return n, units

# matplotlib's YearLocator uses different named
# arguments than the others
LOCATORS = {
    'minute': MinuteLocator,
    'hour': HourLocator,
    'day': DayLocator,
    'week': WeekdayLocator,
    'month': MonthLocator,
    'year': lambda interval: YearLocator(base=interval)
}

def date_breaks(width):
    """
    Regularly spaced dates

    Parameters
    ----------
    width:
        an interval specification. must be one of [minute, hour, day, week, month, year]

    Examples
    --------
    >>> date_breaks(width = '1 year')
    >>> date_breaks(width = '6 weeks')
    >>> date_breaks('months')
    """
    period, units = parse_break_str(width)
    Locator = LOCATORS.get(units)
    locator = Locator(interval=period)
    return locator
