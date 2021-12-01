from entities.book import Book

class StubIOService:
    def read(self):
        with open("src/data/test_books.csv", "r") as f:
            next(f)
            return [Book(*book.split(",")) for book in f]

    def write(self, book):
        with open("src/data/test_books.csv", "a") as f:
            f.write(f"\n{book.author},{book.title},{book.published}")