"""Service for reading from and writing to the items datafile"""
import re
import csv
from entities.book import Book
from entities.video import Video
from entities.blog import Blog

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
        file.write(f"\n{item_type};{item_fields}")

#def get_last_id(fpath):
#    with open(fpath) as f:
#        for r in f: pass
#    return int(r[0])

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