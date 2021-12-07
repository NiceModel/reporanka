"""Service for reading from and writing to the items datafile"""
import re

def read_csv(fpath):
    """Reads from the datafile.

    Returns:
        A tuple of (item type: string, item fields: list)
    """

    with open(fpath, "r", encoding="utf-8") as file:
        next(file)
        return [(item.split(";")[0], re.findall("\'(.+?)\'", item)) for item in file]

def write_csv(fpath, item_type, item_fields):
    """Writes to the datafile.

    Writes in two columns:
        item type: string, item fields: list
    """

    with open(fpath, "a") as file:
        file.write(f"{item_type};{item_fields}\n")

#def get_last_id(fpath):
#    with open(fpath) as f:
#        for r in f: pass
#    return int(r[0])

def clear_csv(fpath):
    """Utility for clearing a csv file completely."""
    f = open(fpath, "w")
    f.write("type;fields")
    f.truncate()
    f.close()

##### TÄÄLLÄ LUULTAVASTI KAIKKI ONGELMA
def delete_csv(fpath, title):
    with open(fpath, "r") as f:
        lines = f.readlines()

    clear_csv(fpath)

    with open(fpath, "w") as f:
        for line in lines:
            if title not in line:
                f.write(line)
        f.truncate()

    # temp = []
    # with open(path) as f:
    #         reader = read_csv(path)
    #         for item in reader:
    #             if item[1][0] != title:
    #                 temp.append(item)
    #         print(temp)
    # with open(path,"w") as fs:
    #     Writer = csv.writer(fs)
    #     Writer.writerows(temp)
    #     print("Tiedosto päivitetty")
    # return temp
