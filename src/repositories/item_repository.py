"""A repository model for storing Book objects"""
from config import DB_PATH
from entities.book import Book
from utilities.csv_utilities import read_csv, write_csv, delete_csv
import csv

class ItemRepository:
    """Repository class for storing Book objects.

    attr:
        fpath: str: path to a csv file where the book database is stored
        books: list: list of Book objects
    """
    def __init__(self, fpath=DB_PATH):
        self._fpath = fpath
        self._items = read_csv(self._fpath)

    def find_all(self):
        """Returns all the books in the repository"""
        return self._items

    def create(self, item_type, item_fields):
        """Creates a new book, takes a Book object as its only argument."""
        """
        if isinstance(book, Book):
            if not self._is_duplicate(book):
                self._items.append(book)
                write_csv(book, self._fpath)
                return book
            return "duplicate"
        raise TypeError(
            f"Object should be <class 'Book'>, but was {type(book)}")
        """
        self._items.append((item_type, item_fields))
        write_csv(self._fpath, item_type, item_fields)

    def _is_duplicate(self, new_item):
        """Checks if a book is already in the repository."""
        for item in self._items:
            if str(item) == str(new_item):
                return True
        return False
        
    def _delete_item(self, item_title):
        self._items = delete_csv(self._fpath, item_title)


ITEM_REPOSITORY = ItemRepository()
