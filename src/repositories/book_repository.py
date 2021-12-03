from config import DB_PATH
from entities.book import Book
from utilities.csv_utilities import read_csv, write_csv


class BookRepository:
    def __init__(self, fpath=DB_PATH):
        self._fpath = fpath
        self._books = read_csv(self._fpath)

    def find_all(self):
        return self._books

    def create(self, book):
        if isinstance(book, Book):
            self._books.append(book)
            write_csv(book, self._fpath)
            return book
        raise TypeError(
            f"Object should be <class 'Book'>, but was {type(book)}")


book_repository = BookRepository()
