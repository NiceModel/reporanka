"""Utility functions for reading from and writing to the items datafile"""

def write_csv(fpath, data):
    """Write to a csv file.

    args:
        fpath: str: path to the file to be written to
    """
    with open(fpath, "a") as f:
        f.write(f"{data}\n")

def read_csv(fpath):
    """Read data from a csv file.

    args:
        fpath: str: path to the file to be read from
    """
    temp = []
    with open(fpath, 'r') as f:
        next(f)
        for row in f:
            row = row.replace('\n', '')
            temp.append((row.split(';')))
    return temp

def clear_csv(fpath):
    """Utility for clearing a csv file completely."""
    f = open(fpath, "w")
    f.write("type;fields\n")
    f.truncate()
    f.close()
