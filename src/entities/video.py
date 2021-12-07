"""Module for Video"""

class Video:
    """Class for describing a video object.

    attr:
        id: int: unique id number for entity
        title: str: title of the video
        address: str: url of the video
        creator: str: publisher of the video
        published: date: publication date of the video
    """
    def __init__(self, creator, title, address, published):
        #self.id = id
        self.title = title
        self.address = address
        self.creator = creator
        self.published = published

    def __str__(self):
        return f"{self.creator}: {self.title}, {self.address}, ({self.published})"