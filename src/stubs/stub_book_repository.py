"""Stub for book repository"""
from config import TEST_DB_PATH
from entities.book import Book
from utilities.csv_utilities import read_csv, write_csv, clear_csv

class StubBookRepository:
    """Stub for book repository"""
    def __init__(self):
        clear_csv(TEST_DB_PATH)
        self._books = read_csv(TEST_DB_PATH)

    def find_all(self):
        """Get all books"""
        return self._books

    def create(self, book):
        """Add book to list and file"""
        if isinstance(book, Book):
            if not self._is_duplicate(book):
                self._books.append(book)
                write_csv(book, TEST_DB_PATH)
                return book
            return "duplicate"
        raise TypeError(
            f"Object should be <class 'Book'>, but was {type(book)}")

    def _is_duplicate(self, new_book):
        """Checks if a book is already in the repository."""
        for book in self._books:
            if str(book) == str(new_book):
                return True
        return False

book_repository = StubBookRepository()
