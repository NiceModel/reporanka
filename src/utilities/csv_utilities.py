from entities.book import Book

def read_csv(fpath):
    temp = []
    with open(fpath) as f:
        for r in f:
            r = r.replace("\n", "")
            temp.append(Book(*r.split(";")))
        return temp

def write_csv(book, fpath):
    with open(fpath, "a") as f:
        f.write(f"\n{book.id};{book.authors};{book.title};{book.published}")

def get_last_id(fpath):
    with open(fpath) as f:
        for r in f: pass
    return int(r[0])

def clear_csv(fpath):
    f = open(fpath, "w")
    f.truncate()
    f.close()

