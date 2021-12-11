"""A repository model for storing Book objects"""
from config import DB_PATH, TEST_DB_PATH
from entities.item import Book, Blog, Video
from utilities.csv_utilities import read_csv, write_csv, delete_csv, clear_csv

class ItemRepository:
    """Repository class for storing Book objects.

    attr:
        fpath: str: path to a csv file where the book database is stored
        items: list: list of reading tips
    """
    def __init__(self, fpath=DB_PATH):
        self._fpath = fpath
        # self._items = read_csv(self._fpath)
        self._items = {}
        self._read_data()

    def create(self, item_type, item_data):
        if item_type == 'book':
            item = Book(*item_data)
        elif item_type == 'blog':
            item = Blog(*item_data)
        elif item_type == 'video':
            item = Video(*item_data)
        else:
            return False
        
        if self._is_duplicate(item):
            return False

        self._items[item.item_id] = item
        return True

    def save(self):
        clear_csv(self._fpath)
        for item in self._items.values():
            write_csv(self._fpath, item.csv_data)

    def delete_item(self, item_id):
        return self._items.pop(item_id, None)

    def _read_data(self):
        data = read_csv(self._fpath)
        for item in data:
            print(item)
            self.create(item[0], (item[1:]))

    def _is_duplicate(self, new_item):
        if not self._items:
            return False
        for item in self._items.values():
            if str(new_item) == str(item):
                return True
        return False

    def list_items(self):
        return [item.info for item in self._items.values()]

    # def find_all(self):
    #     """Returns all the items in the repository"""
    #     return self._items

    # def create(self, item_id, item_type, item_fields):
    #     """Creates a new item.
    #     args:
    #         item_type: str: the category the item belongs to
    #         item_fields: list: data for the item
    #     """
    #     if self._is_duplicate((item_type, item_fields)):
    #         return "duplicate"
    #     self._items.append((item_id, item_type, item_fields))
    #     write_csv(self._fpath, item_id, item_type, item_fields)
    #     return (item_id, item_type, item_fields)

    # def _is_duplicate(self, new_item):
    #     """Checks if an item is already in the repository."""
    #     if new_item in [item[1:] for item in self._items]:
    #         return True
    #     return False
    
    # def delete_all_items(self):
    #     clear_csv(self._fpath)
    #     self._items = read_csv(self._fpath)

    # def delete_item(self, item_title):
    #     delete_csv(self._fpath, item_title)
    #     self._items = read_csv(self._fpath)

ITEM_REPOSITORY = ItemRepository()
TEST_ITEM_REPO = ItemRepository(TEST_DB_PATH)
