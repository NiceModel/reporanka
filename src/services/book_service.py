from models.book import Book
from repositories.book_repository import (
    book_repository as default_book_repository
)


class BookService:
    def __init__(self, book_repository=default_book_repository):
        self._book_repository=book_repository

    def create_book(self, author, title, published):
        book = self._book_repository.create(
            Book(author, title, published)
        )
        return book
    def find_all_books(self):
        books = self._book_repository.find_all()
        return sorted(books, key = lambda book: book.title.lower())

book_service = BookService()