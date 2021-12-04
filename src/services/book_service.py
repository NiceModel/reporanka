from entities.book import Book
from repositories.book_repository import (
    book_repository as default_book_repository
)
from services.id_generator import (id_generator as default_id_generator)


class BookService:
    def __init__(self, book_repository=default_book_repository, id_generator=default_id_generator):
        self._book_repository = book_repository
        self._id_generator = id_generator

    def create_book(self, authors, title, published):
        book_id = self._id_generator.new_id()
        book = self._book_repository.create(
            Book(book_id, authors, title, published)
        )
        return book

    def find_all_books(self):
        books = self._book_repository.find_all()
        return sorted(books, key=lambda book: book.title.lower())


book_service = BookService()
