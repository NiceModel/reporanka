"""Stub for book repository"""
from config import TEST_DB_PATH
from entities.book import Book
from utilities.csv_utilities import read_csv, write_csv

class StubBookRepository:
    """Stub for book repository"""
    def __init__(self):
        self._books = read_csv(TEST_DB_PATH)

    def find_all(self):
        """Get all books"""
        return self._books

    def create(self, book):
        """Add book to list and file"""
        if isinstance(book, Book):
            self._books.append(book)
            write_csv(book, TEST_DB_PATH)
            return book
        raise TypeError(
            f"Object should be <class 'Book'>, but was {type(book)}")


book_repository = StubBookRepository()
