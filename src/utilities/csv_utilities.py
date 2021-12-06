from entities.book import Book
from entities.video import Video
from entities.blog import Blog

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

def read_videos_csv(path):
    temp = []
    with open(path) as f:
        for r in f:
            r = r.replace("\n", "")
            temp.append(Video(*r.split(";")))
        return temp

def write_videos_csv(video, path):
    with open(path, "a") as f:
        f.write(f"\n{video.id};{video.title};{video.address};{video.creator};{video.published}")

def read_blogs_csv(path):
    temp = []
    with open(path) as f:
        for r in f:
            r = r.replace("\n", "")
            temp.append(Blog(*r.split(";")))
        return temp

def write_blogs_csv(blog, path):
    with open(path, "a") as f:
        f.write(f"\n{blog.id};{blog.name};{blog.post};{blog.address};{blog.blogger};{blog.published}")