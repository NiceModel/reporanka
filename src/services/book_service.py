"""Module for a book service to connect a book repository to the application."""

from entities.book import Book
from repositories.book_repository import (
    BOOK_REPOSITORY as default_book_repository
)

class BookService:
    """Class for a book service.

    attr:
        book_repository: BookRepository: repository object where the books are stored
    """
    def __init__(self, book_repository=default_book_repository):
        self._book_repository = book_repository

    def create_book(self, author, title, published):
        """Creates a new book.

        args:
            author: str: author of the book
            title: str: title of the book
            published: str: year of publication of the book
        """
        book = self._book_repository.create(
            Book(author, title, published)
        )
        return book

    def find_all_books(self):
        """Returns an alphabetically sorted list of all books."""
        books = self._book_repository.find_all()
        return sorted(books, key=lambda book: book.title.lower())

BOOK_SERVICE = BookService()
