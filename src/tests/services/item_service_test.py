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
        item_type = "book"
        item_fields = ["Dune", "Frank", "Herbert", "1965"]
        self.item_service.create_item(item_type, item_fields)

        book = self.item_service.find_all_items()[0]
        print(book)

        self.assertEqual(book[1][1], "Frank")
        self.assertEqual(book[1][2], "Herbert")
        self.assertEqual(book[1][0], "Dune")
        self.assertEqual(book[1][3], "1965")

    def test_find_all_items_returns_alphabetically(self):
        item_type = "book"
        item_fields = ["Dune", "Frank", "Herbert", "1965"]
        self.item_service.create_item(item_type, item_fields)
        item_fields = ["The Hitchhiker's Guide to the Galaxy", "Douglas", "Adams", "1979"]
        self.item_service.create_item(item_type, item_fields)
        item_fields = ["The Fellowship of the Ring", "J. R. R.", "Tolkien", "1954"]
        self.item_service.create_item(item_type, item_fields)

        books = self.item_service.find_all_items()
        #book_titles_alphabetic = [
        #    "Dune", "The Fellowship of the Ring", "The Hitchhiker's Guide to the Galaxy"]
        book_lastnames_alphabetic = ["Adams", "Herbert", "Tolkien"]

        for book, book_alphabetic in zip(books, book_lastnames_alphabetic):
            self.assertEqual(book[1][2], book_alphabetic)
