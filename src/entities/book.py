class Book:
    def __init__(self, author, title, published):
        self.author = author
        self.title = title
        self.published = published

    def __str__(self):
        return f"{self.author}: {self.title} ({self.published})"
