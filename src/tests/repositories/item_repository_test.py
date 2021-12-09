import unittest
from config import TEST_DB_PATH
from repositories.item_repository import ItemRepository
from utilities.csv_utilities import clear_csv


class TestItemRepository(unittest.TestCase):
    def setUp(self):
        clear_csv(TEST_DB_PATH)
        self.item_repo = ItemRepository(TEST_DB_PATH)
        self.test_item = (0, 'test', ['author', 'title', 'published'])
        self.type = self.test_item[1]
        self.fields = self.test_item[2]

    def test_initialises_repo(self):
        self.assertTrue(isinstance(self.item_repo._items, list))

    def test_create_item(self):
        new_item = self.item_repo.create(0, self.type, self.fields)
        self.assertEqual(new_item, self.test_item)

    def test_create_duplicate_item(self):
        self.item_repo.create(0, self.type, self.fields)
        new_item = self.item_repo.create(0, self.type, self.fields)
        self.assertEqual(new_item, 'duplicate')

    def test_find_all_empty(self):
        items = self.item_repo.find_all()
        self.assertEqual(len(items), 0)
        self.assertTrue(isinstance(items, list))

    def test_find_all_not_empty(self):
        self.item_repo.create(0, self.type, self.fields)
        items = self.item_repo.find_all()
        self.assertEqual(len(items), 1)

    def test_duplicate_not_added_to_items(self):
        self.item_repo.create(0, self.type, self.fields)
        self.item_repo.create(0, self.type, self.fields)
        items = self.item_repo.find_all()
        self.assertEqual(len(items), 1)