"""Service for reading from and writing to the items datafile"""
import re
import csv

def read_csv(fpath):
    """Reads from the datafile.

    Returns:
        A tuple of (item type: string, item fields: list)
    """

    with open(fpath, "r") as file:
        next(file)
        return [(item.split(";")[0][1:], re.findall("\'(.+?)\'", item)) for item in file]

def write_csv(fpath, item_type, item_fields):
    """Writes to the datafile.

    Writes in two columns:
        item type: string, item fields: list
    """

    with open(fpath, "a") as file:
        file.write(f"\n{item_type};{item_fields}")

#def get_last_id(fpath):
#    with open(fpath) as f:
#        for r in f: pass
#    return int(r[0])

def clear_csv(fpath):
    f = open(fpath, "w")
    f.truncate()
    f.close()

