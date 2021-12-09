import unittest
from config import TEST_DB_PATH
from services.item_service import ItemService
from repositories.item_repository import ItemRepository
from utilities.csv_utilities import clear_csv


class TestBookRepository(unittest.TestCase):
    def setUp(self):
        clear_csv(TEST_DB_PATH)
        self.item_service = ItemService(ItemRepository(TEST_DB_PATH))

    def test_init_item_service(self):
        self.assertTrue(isinstance(self.item_service, ItemService))

    def test_create_item(self):
        item_type = "book"
        item_fields = ["Meri", "Meemikirja", "2021"]
        self.item_service.create_item(item_type, item_fields)
        expected = "(4, 'book', ['Meri', 'Meemikirja', '2021'])"
        self.assertEqual(str(self.item_service.find_all_items()[0]), expected)

    def test_find_all_items(self):
        books = self.item_service.find_all_items()
        self.assertTrue(isinstance(books, list))

    def test_create_item_returns_correct_book(self):
        item_type = "book"
        item_fields = ["Frank Herbert", "Dune", "1965"]
        self.item_service.create_item(item_type, item_fields)

        book = self.item_service.find_all_items()[0]
        print(book)

        self.assertEqual(book[2][0], "Frank Herbert")
        self.assertEqual(book[2][1], "Dune")
        self.assertEqual(book[2][2], "1965")

    def test_find_all_items_returns_alphabetically(self):
        item_type = "book"
        item_fields = ["Frank Herbert", "Dune", "1965"]
        self.item_service.create_item(item_type, item_fields)
        item_fields = ["Douglas Adams", "The Hitchhiker's Guide to the Galaxy", "1979"]
        self.item_service.create_item(item_type, item_fields)
        item_fields = ["J.R.R. Tolkien", "The Fellowship of the Ring", "1954"]
        self.item_service.create_item(item_type, item_fields)

        books = self.item_service.find_all_items()
        book_names_alphabetic = ["Douglas Adams", "Frank Herbert", "J.R.R. Tolkien"]

        for book, book_alphabetic in zip(books, book_names_alphabetic):
            self.assertEqual(book[2][0], book_alphabetic)
