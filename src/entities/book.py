"""Module for Book objects"""

class Book:
    """Class for describing a book object.

    attr:
        id: int: unique id number for entity
        authors: list: list of authors of the book
        title: str: the title of the book
        published: str: the publication year of the book
    """
    def __init__(self, id, authors, title, published):
        self.id = id
        self.authors = authors
        self.title = title
        self.published = published

    def __str__(self):
        return f"{self.authors}: {self.title} ({self.published})"
