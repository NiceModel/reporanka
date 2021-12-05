"""Module for a book service to connect a book repository to the application."""

from entities.book import Book
from repositories.item_repository import (
    ITEM_REPOSITORY as default_item_repository
)
#from services.id_generator import (id_generator as default_id_generator)

class ItemService:
    """Class for a book service.

    attr:
        book_repository: BookRepository: repository object where the books are stored
        id_generator: IdGenerator: generator for id numbers
    """
    def __init__(self, item_repository=default_item_repository):
        self._item_repository = item_repository
        #self._id_generator = id_generator

    def create_item(self, item_type, item_fields):
        """Creates a new book.

        args:
            authors: list: authors of the book
            title: str: title of the book
            published: str: year of publication of the book
        """
        item = self._item_repository.create(
            item_type,
            item_fields
        )
        return item

    def find_all_items(self):
        """Returns list of all items first sorted by item type and then by author lastname"""
        items = self._item_repository.find_all()
        items_sorted = sorted(items, key=lambda item: (item[0], item[1][2]))

        return items_sorted

ITEM_SERVICE = ItemService()
