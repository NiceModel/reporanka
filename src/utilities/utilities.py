"""Utility functions"""

from datetime import date

def check_year(year):
    """Checks for the validity of 'year' input"""
    if not year:
        return None

    bce = ["bce", "bc", "eaa", "ekr"]
    year_split = year.split()

    if not year_split:
        return False

    if len(year_split) > 1:
        for suffix in bce:
            if year_split[1].find(suffix):
                try:
                    year_int = int(year_split[0])
                except ValueError:
                    return False
                return True

    try:
        year_int = int(year_split[0])
    except ValueError:
        return False

    return bool(0 <= year_int <= date.today().year)
