from entities.book import Book

class BookRepository:
    def __init__(self):
        self._books = []

    def find_all(self):
        return self._books

    def create(self, book):
        if isinstance(book, Book):
            self._books.append(book)
            return True
        raise TypeError(f"Object type should be 'Book', but was {type(book)}")

book_repository = BookRepository()