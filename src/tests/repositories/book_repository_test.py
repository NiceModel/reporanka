import unittest
from config import TEST_DB_PATH
from repositories.item_repository import ItemRepository
from entities.book import Book
from utilities.csv_utilities import clear_csv


class TestItemRepository(unittest.TestCase):
    def setUp(self):
        clear_csv(TEST_DB_PATH)
        self.item_repo = ItemRepository(TEST_DB_PATH)

    def test_initialises_repo(self):
        self.assertTrue(isinstance(self.item_repo._items, tuple))

    """
    def test_creates_book_if_book_object(self):
        book = Book("Meri", "Meemikirja", "2021")
        self.assertTrue(isinstance(self.item_repo.create(book), Book))

    def test_create_book_not_book_obj(self):
        book = "olen kirja"
        with self.assertRaises(TypeError) as cm:
            self.item_repo.create(book)
        actual = cm.exception
        self.assertTrue(isinstance(actual, TypeError))
        """

    def test_find_all_empty(self):
        books = self.item_repo.find_all()
        self.assertEqual(len(books), 0)
        self.assertTrue(isinstance(books, tuple))

    """
    def test_find_all_not_empty(self):
        book = Book("Meri", "Meemikirja", "2021")
        self.item_repo.create(book)
        books = self.item_repo.find_all()
        self.assertEqual(len(books), 1)
        self.assertTrue(isinstance(books, list))

    def test_duplicate_not_added(self):
        book = Book("Meri", "Meemikirja", "2021")
        self.item_repo.create(book)
        book = Book("Meri", "Meemikirja", "2021")
        self.item_repo.create(book)
        books = self.item_repo.find_all()
        self.assertEqual(len(books), 1)
        self.assertTrue(isinstance(books, list))
    """