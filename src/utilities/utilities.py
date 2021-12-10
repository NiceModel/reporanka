"""Utility functions"""

from datetime import date
from string import ascii_lowercase, digits
import secrets

def generate_id():
    """Generates a random alphanumeric four-character identifier"""
    chars = ascii_lowercase + digits
    return ''.join(secrets.choice(chars) for _ in range(4))

def check_year(year):
    """Checks for the validity of 'year' input"""
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
