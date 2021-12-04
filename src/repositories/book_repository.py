from entities.book import Book
from services.io_service import IOService


class BookRepository:
    def __init__(self, io=IOService()):
        self.io = io
        self._books = io.read()

    def find_all(self):
        return self._books

    def create(self, book):
        if isinstance(book, Book):
            self._books.append(book)
            self.io.write(book)
            return book
        raise TypeError(
            f"Object should be <class 'Book'>, but was {type(book)}")


book_repository = BookRepository()