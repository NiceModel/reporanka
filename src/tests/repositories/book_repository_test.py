import unittest
from repositories.book_repository import BookRepository
from entities.book import Book

class TestBookRepository(unittest.TestCase):
    def setUp(self):
        self.book_repo = BookRepository()

    def test_initialises_repo(self):
        self.assertTrue(isinstance(self.book_repo._books, list))

    def test_creates_book_if_book_object(self):
        book = Book("Meri", "Meemikirja", "2021")
        self.assertTrue(isinstance(self.book_repo.create(book), Book))

    def test_create_book_not_book_obj(self):
        book = "olen kirja"
        with self.assertRaises(TypeError) as cm:
            self.book_repo.create(book)
        actual = cm.exception
        self.assertTrue(isinstance(actual, TypeError))

    def test_find_all_empty(self):
        books = self.book_repo.find_all()
        self.assertEqual(len(books), 0)
        self.assertTrue(isinstance(books, list))

    def test_find_all_not_empty(self):
        book = Book("Meri", "Meemikirja", "2021")
        self.book_repo.create(book)
        books = self.book_repo.find_all()
        self.assertEqual(len(books), 1)
        self.assertTrue(isinstance(books, list))