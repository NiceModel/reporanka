from entities.book import Book
from stub_io_service import StubIOService

class StubBookRepository:
    def __init__(self, io = StubIOService()):
        self.io = io
        self._books = io.read()

    def find_all(self):
        return self._books

    def create(self, book):
        if isinstance(book, Book):
            self._books.append(book)
            self.io.write(book)
            return book
        raise TypeError(f"Object should be <class 'Book'>, but was {type(book)}")

book_repository = StubBookRepository()