class Book:
    def __init__(self, id, authors, title, published):
        self.id = id
        self.authors = authors
        self.title = title
        self.published = published

    def __str__(self):
        return f" {self.id}: {self.title} ({self.published})\n    {self.authors}"
