"""Module for Book objects"""

class Book:
    """Class for describing a book object.

    attr:
        author: str: the author of the book
        title: str: the title of the book
        published: str: the publication year of the book
    """
    def __init__(self, author, title, published):
        self.author = author
        self.title = title
        self.published = published

    def __str__(self):
        return f"{self.author}: {self.title} ({self.published})"
