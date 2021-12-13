import unittest
from config import TEST_DB_PATH
from services.item_service import ItemService
from repositories.item_repository import ItemRepository
from utilities.csv_utilities import clear_csv, read_csv

TEST_ITEMS = [
    ("book", ["Naomi Klein", "No Logo", "1999", "0001"]),
    ("blog", [
        "Tamsin", "Cupful of Kale", "Tofu Katsu Curry",
        "https://cupfulofkale.com/vegan-tofu-katsu-curry/", "1.1.2022",
        "0002"
        ]),
    ("video", [
        "Lee Suhyun", "LEE SUHYUN - 'ALIEN' SELF M/V (YOUTUBE EDITION)",
        "https://youtu.be/t33wNZJf4Pk", "23.10.2020", "0003"
    ]),
    ("book", ["Frank Herbert", "Dune", "1965", "0004"]),
    ("blog", [
        "Pedro Medeiros", "Pixel Grimoire", "How to start making pixel art #6",
        "https://medium.com/pixel-grimoire/how-to-start-making-pixel-art-6-a74f562a4056", "8.1.2019",
        "0005"
    ]),
    ("video", [
        "tglab", "Early mitotic divisions in a Drosophila embryo",
        "https://youtu.be/XSKh-GLQn4E", "3.8.2008", "0006"
    ])
]

class TestItemService(unittest.TestCase):
    def setUp(self):
        clear_csv(TEST_DB_PATH)
        self.item_service = ItemService(ItemRepository(TEST_DB_PATH))

    def _create_test_items(self):
        for item in TEST_ITEMS:
            self.item_service.create_item(item[0], item[1])

    def test_init_item_service(self):
        self.assertTrue(isinstance(self.item_service, ItemService))

    def test_create_book(self):
        item_type = "book"
        item_fields = TEST_ITEMS[0][1]
        self.item_service.create_item(item_type, item_fields)
        item = self.item_service.list_by_type_alphabetically()[0]
        expected = ["book", "0001", "Naomi Klein", "No Logo"]
        self.assertEqual(item, expected)

    def test_create_blog(self):
        item_type = 'blog'
        item_fields = TEST_ITEMS[1][1]
        self.item_service.create_item(item_type, item_fields)
        item = self.item_service.list_by_type_alphabetically()[0]
        self.assertEqual(item[1], "0002")

    def test_create_video(self):
        item_type = 'video'
        item_fields = TEST_ITEMS[2][1]
        self.item_service.create_item(item_type, item_fields)
        item = self.item_service.list_by_type_alphabetically()[0]
        self.assertEqual(item[1], "0003")

    def test_list_items_returns_list(self):
        items = self.item_service.list_by_type_alphabetically()
        self.assertTrue(isinstance(items, list))

    def test_list_returns_items_in_correct_order(self):
        self._create_test_items()
        items = self.item_service.list_by_type_alphabetically()
        correct_order = [
            "Pedro Medeiros", "Tamsin", "Frank Herbert",
            "Naomi Klein", "Lee Suhyun", "tglab"
            ]
        for item, expected in zip(items, correct_order):
            self.assertEqual(item[2], expected)

    def test_delete_item(self):
        self._create_test_items()
        self.item_service.delete_item('0001')
        items = self.item_service.list_by_type_alphabetically()
        self.assertEqual(len(items), len(TEST_ITEMS)-1)
    
    def test_clear(self):
        self._create_test_items()
        self.item_service.clear()
        items = self.item_service.list_by_type_alphabetically()
        self.assertEqual(len(items), 0)

    def test_save_file(self):
        self._create_test_items()
        self.item_service.save()
        data = read_csv(TEST_DB_PATH)
        self.assertEqual(len(data), 6)

    def test_find_by_id_returns_correct_item(self):
        self._create_test_items()
        item = self.item_service.find_by_id('0001')
        self.assertEqual(item['id'], '0001')
