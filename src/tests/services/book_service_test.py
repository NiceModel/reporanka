import unittest
from config import TEST_DB_PATH
from services.item_service import ItemService
from repositories.item_repository import ItemRepository
from utilities.csv_utilities import clear_csv


class TestBookRepository(unittest.TestCase):
    def setUp(self):
        clear_csv(TEST_DB_PATH)
        self.item_service = ItemService(ItemRepository(TEST_DB_PATH))

    def test_init_book_service(self):
        self.assertTrue(isinstance(self.item_service, ItemService))

    def test_create_item(self):
        book = self.item_service.create_item(
            "Meri", "Meemikirja", "2021"
        )
        expected = "Meri: Meemikirja (2021)"
        self.assertEqual(str(book), expected)

    def test_find_all_items(self):
        books = self.item_service.find_all_items()
        self.assertTrue(isinstance(books, list))

    def test_create_item_returns_correct_book(self):
        book = self.item_service.create_item("Frank Herbert", "Dune", "1965")

        self.assertEqual(book.author, "Frank Herbert")
        self.assertEqual(book.title, "Dune")
        self.assertEqual(book.published, "1965")

    def test_find_all_items_returns_alphabetically(self):
        self.item_service.create_item("Frank Herbert", "Dune", "1965")
        self.item_service.create_item(
            "Douglas Adams", "The Hitchhiker's Guide to the Galaxy", "1979")
        self.item_service.create_item(
            "J. R. R. Tolkien", "The Fellowship of the Ring", "1954")

        books = self.item_service.find_all_items()
        book_titles_alphabetic = [
            "Dune", "The Fellowship of the Ring", "The Hitchhiker's Guide to the Galaxy"]
        for book, book_alphabetic in zip(books, book_titles_alphabetic):
            self.assertEqual(book.title, book_alphabetic)
