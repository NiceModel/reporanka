"""Module for item storing."""
from config import DB_PATH
from entities.item import Book, Blog, Video
from utilities.csv_utilities import read_csv, write_csv, clear_csv

class ItemRepository:
    """Repository class for storing Item objects.

    attr:
        fpath: str: path to a csv file where the item database is stored
        items: dict: list of reading tips; key: item id, val: Item object
    """
    def __init__(self, fpath=DB_PATH):
        self._fpath = fpath
        self._items = {}
        self._read_data()

    def create(self, item_type, item_data):
        """Creates a new object. Returns True if item is added
        to the repoitory, otherwise false.

        args:
            item_type: str: type of the item (book/blog/video)
            item_data: list: information about the item in list form
        """
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
        """Clears the csv file and saves the new information."""
        clear_csv(self._fpath)
        for item in self._items.values():
            write_csv(self._fpath, item.csv_data)

    def delete_item(self, item_id):
        """Deletes an item from the repository.

        args:
            item_id: str: unique identifier of the item.
        return:
            Item object if item exists, otherwise None
        """
        return self._items.pop(item_id, None)

    def _read_data(self):
        """Reads item data from a csv file."""
        data = read_csv(self._fpath)
        for item in data:
            self.create(item[0], (item[1:]))

    def _is_duplicate(self, new_item):
        """Checks if given item already exists.

        args:
            new_item: Item object
        return:
            bool: True if item is in repository, otherwise False
        """
        if not self._items:
            return False
        for item in self._items.values():
            if str(new_item) == str(item):
                return True
        return False

    def list_items(self):
        """Returns a list with the items' basic info."""
        return [item.info for item in self._items.values()]

    def delete_all_items(self):
        """Clears the csv file and deletes all items from the repository."""
        clear_csv(self._fpath)
        self._items = {}

    def find_by_id(self, item_id):
        """Searches for an item by its id.

        args:
            item_id: str: item to be searched
        return:
            item details (dict) if item exists, otherwise None
        """
        for key, val in self._items.items():
            if key == item_id:
                return val.details
        return None

ITEM_REPOSITORY = ItemRepository()
