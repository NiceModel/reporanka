"""Module for a book service to connect a book repository to the application."""

from entities.book import Book
from repositories.book_repository import (
    BOOK_REPOSITORY as default_book_repository
)
from services.id_generator import (id_generator as default_id_generator)

class BookService:
    """Class for a book service.

    attr:
        book_repository: BookRepository: repository object where the books are stored
        id_generator: IdGenerator: generator for id numbers
    """
    def __init__(self, book_repository=default_book_repository, id_generator=default_id_generator):
        self._book_repository = book_repository
        self._id_generator = id_generator

    def create_book(self, authors, title, published):
        """Creates a new book.

        args:
            authors: list: authors of the book
            title: str: title of the book
            published: str: year of publication of the book
        """
        book_id = self._id_generator.new_id()
        book = self._book_repository.create(
            Book(book_id, authors, title, published)
        )
        return book

    def find_all_books(self):
        """Returns an alphabetically sorted list of all books."""
        books = self._book_repository.find_all()
        return sorted(books, key=lambda book: book.title.lower())

BOOK_SERVICE = BookService()
