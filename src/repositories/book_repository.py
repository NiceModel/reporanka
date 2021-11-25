from models.book import Book

class BookRepository:
    def __init__(self):
        self._books = []

    def find_all(self):
        return self._books

    def create(self,book):
       
        self._books.append(book)
        return book

book_repository = BookRepository()