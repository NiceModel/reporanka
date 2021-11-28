from datetime import date

def check_year(year):
    if not year:
        return None

    bce = ["bce", "bc", "eaa", "ekr"]
    year_split = year.split()

    if not year_split:
        return False
    elif len(year_split) > 1:
        for s in bce:
            if year_split[1].find(s):
                try:
                    yr = int(year_split[0])
                except ValueError:
                    return False
                return True

    try:
        yr = int(year_split[0])
    except ValueError:
        return False

    if 0 <= yr <= date.today().year:
        return True

    return False
