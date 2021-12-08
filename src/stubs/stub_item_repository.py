"""Stub for item repository"""
from config import TEST_DB_PATH
from utilities.csv_utilities import read_csv, write_csv, clear_csv, delete_csv

class StubItemRepository:
    """Stub for book repository"""
    def __init__(self):
        clear_csv(TEST_DB_PATH)
        self._items = read_csv(TEST_DB_PATH)
        self._fpath = TEST_DB_PATH

    def find_all(self):
        """Get all books"""
        return self._items

    def create(self, item_type, item_fields):
        """Creates a new item.
        args:
            item_type: str: the category the item belongs to
            item_fields: list: data for the item
        """
        if self._is_duplicate((item_type, item_fields)):
            return "duplicate"
        self._items.append((item_type, item_fields))
        write_csv(TEST_DB_PATH, item_type, item_fields)
        return (item_type, item_fields)

    def _is_duplicate(self, new_item):
        """Checks if an item is already in the repository."""
        if new_item in self._items:
            return True
        return False

    def _delete_item(self, item_title):
        """Deletes a certain item from repository."""
        delete_csv(self._fpath, item_title)
        self._items = read_csv(self._fpath)

ITEM_REPOSITORY = StubItemRepository()
