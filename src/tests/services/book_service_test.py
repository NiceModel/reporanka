import unittest
from services.book_service import BookService

class TestBookRepository(unittest.TestCase):
    def setUp(self):
        self.book_service = BookService()

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
