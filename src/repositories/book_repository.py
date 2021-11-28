from entities.book import Book

class BookRepository:
    def __init__(self):
        with open("src/data/books.csv", "r") as f:
            next(f)
            #print([book.split(",") for book in f])
            #raise Exception
            self._books = [Book(*book.split(",")) for book in f]

    def find_all(self):
        return self._books

    def create(self, book):
        if isinstance(book, Book):
            self._books.append(book)
            return book
        raise TypeError(f"Object should be <class 'Book'>, but was {type(book)}")

book_repository = BookRepository()