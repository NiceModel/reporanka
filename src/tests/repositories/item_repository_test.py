import unittest
from config import TEST_DB_PATH
from repositories.item_repository import ItemRepository
from utilities.csv_utilities import clear_csv, read_csv


class TestItemRepository(unittest.TestCase):
    def setUp(self):
        clear_csv(TEST_DB_PATH)
        self.item_repo = ItemRepository(TEST_DB_PATH)
        self.book = ['Patrick Ness', 'The Knife of Never Letting Go', '2008', '0001']
        self.blog = [
            'Eero Tarmo', 'Soundi.fi',
            'Androgyyniä laulua ja irtonaista kävelyä – tältä kuulostaa Arto Tuunelan kevät',
            'https://www.soundi.fi/jutut/pariisin-kevat-nokkamies-kasasi-kevat-aiheisen-soittolistan/',
            '13.3.2016', '0002'
        ]
        self.video = [
            'Christian Duenas', 'Pygame Menu System Tutorial Part 2: Building the Menu and States',
            'https://youtu.be/bmRFi7-gy5Y', '24.7.2020', '0003'
        ]
        self.item = ["Pablo Picasso", "Ls Demoiselles d'Avignon", "1907"]

    def test_initialises_repo(self):
        self.assertTrue(isinstance(self.item_repo._items, dict))

    def test_create_book(self):
        book = self.item_repo.create('book', self.book)
        self.assertTrue(book)

    def test_create_blog(self):
        blog = self.item_repo.create('blog', self.blog)
        self.assertTrue(blog)

    def test_create_video(self):
        video = self.item_repo.create('video', self.video)
        self.assertTrue(video)

    def test_create_nonexisting_type(self):
        item = self.item_repo.create('painting', self.item)
        self.assertFalse(item)

    def test_create_duplicate_item(self):
        self.item_repo.create('book', self.book)
        new_item = self.item_repo.create('book', self.book)
        self.assertFalse(new_item)

    def test_list_items_empty(self):
        items = self.item_repo.list_items()
        self.assertEqual(len(items), 0)

    def test_list_items_not_empty(self):
        self.item_repo.create('book', self.book)
        items = self.item_repo.list_items()
        self.assertEqual(len(items), 1)

    def test_duplicate_not_added_to_items(self):
        self.item_repo.create('book', self.book)
        self.item_repo.create('book', self.book)
        items = self.item_repo.list_items()
        self.assertEqual(len(items), 1)

    def test_delete_item(self):
        self.item_repo.create('book', self.book)
        self.item_repo.create('blog', self.blog)
        self.item_repo.create('video', self.video)
        self.item_repo.delete_item('0001')
        items = self.item_repo.list_items()
        for item in items:
            self.assertNotEqual(item[1], '0001')

    def test_save_file_not_empty(self):
        self.item_repo.create('book', self.book)
        self.item_repo.create('blog', self.blog)
        self.item_repo.create('video', self.video)
        self.item_repo.save()
        data = read_csv(TEST_DB_PATH)
        self.assertEqual(len(data), 3)

    def test_delete_all(self):
        self.item_repo.create('book', self.book)
        self.item_repo.create('blog', self.blog)
        self.item_repo.create('video', self.video)
        self.item_repo.delete_all_items()
        items = self.item_repo.list_items()
        self.assertFalse(items)

    def test_find_existing_item(self):
        self.item_repo.create('book', self.book)
        item = self.item_repo.find_by_id('0001')
        self.assertEqual(item['id'], '0001')

    def test_find_nonexisting_item_empty_repo(self):
        self.assertIsNone(self.item_repo.find_by_id('0004'))

    def test_find_nonexisting_item_nonempty_repo(self):
        self.item_repo.create('book', self.book)
        self.assertIsNone(self.item_repo.find_by_id('0004'))
