"""Stub for item repository"""
from config import TEST_DB_PATH
from entities.item import Book, Blog, Video
from utilities.csv_utilities import read_csv, write_csv, clear_csv

class StubItemRepository:
    """Stub for book repository"""
    def __init__(self):
        self._fpath = TEST_DB_PATH
        self._items = {}
        self._id = 1001

    def create(self, item_type, item_data):
        item_data.append(str(self._id))
        self._id +=1
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
        return [str(item) for item in self._items.values()]

    def delete_all_items(self):
        clear_csv(self._fpath)
        self._items = {}

ITEM_REPOSITORY = StubItemRepository()
