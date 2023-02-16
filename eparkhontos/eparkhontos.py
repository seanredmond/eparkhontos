from eparkhontos.__version__ import __version__
import re

class UnparseableDateError(Exception):
    pass


def to_astronomical(year, is_bce=True):
    """Convert a calendar year to an astronomcial year

    Parameters:
    year -- The year to convert
    is_bce -- If True treat the year as a year BCE (default: True)

    Convert a simpler calendar year to an astronomical year -- BCE years are negative and 1 BCE is 0. year must be an int or something that is convertable to an int.
    """
    try:
        if is_bce:
            return int(year) * -1 + 1

        return int(year)
    except ValueError:
        msg = f"Could not convert date '{year}'"
        if "/" in year:
            raise UnparseableDateError(
                msg
                + ". This looks like it may be an arkhon year. Use from_arkhon() to convert to an astronomical year"
            )

        raise UnparseableDateError(msg)


def to_arkhon(year, with_era=False, prefix_era=False):
    """Convert an astronomical year to a formatted arkhon year string.

    Parameters:
    year (int) -- year to convert. Must be an astronomical year
    with_era (bool) -- If True, append era ("BCE" or "CE") to output
    prefix_era (bool) -- If True (and with_era is True) prepend era to output
    """
    fmt_year = __fmt_arkhon(year)
    era = "BCE" if year < 1 else " CE"

    if with_era:
        if prefix_era:
            return f"{era} {fmt_year}"

        return f"{fmt_year} {era}"

    return fmt_year


def parse_arkhon(year):
    """Parse an arkhon year string and return an astronomical year

    Parameters
    year (str) -- An archon year

    The archon should be two years (any number of digits) separated by a slash ('/') or dash ('-'). If the string contains BCE, BC, CE, AD, upper- or lower-case, with or without periods, this will be be used to determine whether the date should be treated as BCE or CE. Otherwise it will be treated as BCE.
    """

    parsed = re.match(r"^(\d+)[/-](\d+) ?(BCE?|CE|AD)?$", year.upper().replace(".", ""))

    if parsed is None:
        raise UnparseableDateError(f"Could not convert date '{year}'")

    if parsed[3] in ("CE", "AD"):
        return int(parsed[1])

    return to_astronomical(parsed[1])


def version():
    return __version__


def __fmt_arkhon(year):
    """Format astronomical year as an arkhon year"""
    if year < 0:
        return f"{year * -1 + 1}/{year * -1}"

    return f"{year}/{year + 1}"


