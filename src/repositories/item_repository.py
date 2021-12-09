"""A repository model for storing Book objects"""
from config import DB_PATH
from utilities.csv_utilities import read_csv, write_csv, delete_csv

class ItemRepository:
    """Repository class for storing Book objects.

    attr:
        fpath: str: path to a csv file where the book database is stored
        items: list: list of reading tips
    """
    def __init__(self, fpath=DB_PATH):
        self._fpath = fpath
        self._items = read_csv(self._fpath)

    def find_all(self):
        """Returns all the items in the repository"""
        return self._items

    def create(self, id, item_type, item_fields):
        """Creates a new item.
        args:
            item_type: str: the category the item belongs to
            item_fields: list: data for the item
        """
        if self._is_duplicate((item_type, item_fields)):
            return "duplicate"
        self._items.append((id, item_type, item_fields))
        write_csv(self._fpath, id, item_type, item_fields)
        return (id, item_type, item_fields)

    def _is_duplicate(self, new_item):
        """Checks if an item is already in the repository."""
        if new_item in self._items:
            return True
        return False

    def _delete_item(self, item_title):
        delete_csv(self._fpath, item_title)
        self._items = read_csv(self._fpath)

ITEM_REPOSITORY = ItemRepository()
