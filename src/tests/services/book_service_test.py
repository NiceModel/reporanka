import unittest
from config import TEST_DB_PATH
from services.book_service import BookService
from repositories.book_repository import BookRepository
from utilities.csv_utilities import clear_csv


class TestBookRepository(unittest.TestCase):
    def setUp(self):
        clear_csv(TEST_DB_PATH)
        self.book_service = BookService(BookRepository(TEST_DB_PATH))

    def test_init_book_service(self):
        self.assertTrue(isinstance(self.book_service, BookService))

    def test_create_book(self):
        book = self.book_service.create_book(
            "Meri", "Meemikirja", "2021"
        )
        expected = "Meri: Meemikirja (2021)"
        self.assertEqual(str(book), expected)

    def test_find_all_books(self):
        books = self.book_service.find_all_books()
        self.assertTrue(isinstance(books, list))

    def test_create_book_returns_correct_book(self):
        book = self.book_service.create_book("Frank Herbert", "Dune", "1965")

        self.assertEqual(book.author, "Frank Herbert")
        self.assertEqual(book.title, "Dune")
        self.assertEqual(book.published, "1965")

    def test_find_all_books_returns_alphabetically(self):
        self.book_service.create_book("Frank Herbert", "Dune", "1965")
        self.book_service.create_book(
            "Douglas Adams", "The Hitchhiker's Guide to the Galaxy", "1979")
        self.book_service.create_book(
            "J. R. R. Tolkien", "The Fellowship of the Ring", "1954")

        books = self.book_service.find_all_books()
        book_titles_alphabetic = [
            "Dune", "The Fellowship of the Ring", "The Hitchhiker's Guide to the Galaxy"]
        for book, book_alphabetic in zip(books, book_titles_alphabetic):
            self.assertEqual(book.title, book_alphabetic)
