"""A repository model for storing Book objects"""
from config import DB_PATH
from entities.book import Book
from utilities.csv_utilities import read_csv, write_csv

class BookRepository:
    """Repository class for storing Book objects.

    attr:
        fpath: str: path to a csv file where the book database is stored
        books: list: list of Book objects
    """
    def __init__(self, fpath=DB_PATH):
        self._fpath = fpath
        self._books = read_csv(self._fpath)

    def find_all(self):
        """Returns all the books in the repository"""
        return self._books

    def create(self, book):
        """Creates a new book, takes a Book object as its only argument."""
        if isinstance(book, Book):
            if not self._is_duplicate(book):
                self._books.append(book)
                write_csv(book, self._fpath)
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

BOOK_REPOSITORY = BookRepository()
