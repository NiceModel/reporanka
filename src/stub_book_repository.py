"""Stub for book repository"""
from entities.book import Book
from stub_io_service import StubIOService

class StubBookRepository:
    """Stub for book repository"""
    def __init__(self, io=StubIOService()):
        self.io = io
        self._books = io.read()

    def find_all(self):
        """Get all books"""
        return self._books

    def create(self, book):
        """Add book to list and file"""
        if isinstance(book, Book):
            self._books.append(book)
            self.io.write(book)
            return book
        raise TypeError(
            f"Object should be <class 'Book'>, but was {type(book)}")


book_repository = StubBookRepository()
