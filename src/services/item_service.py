"""Module for an item service to connect an item repository to the application."""
from repositories.item_repository import (
    ITEM_REPOSITORY as default_item_repository
)
class ItemService:
    """Class for item service.

    attr:
        item_repository: ItemRepository: repository object where the books are stored
        id_generator: IdGenerator: generator for id numbers
    """
    def __init__(self, item_repository=default_item_repository):
        self._item_repository = item_repository

    def create_item(self, item_type, item_data):
        return self._item_repository.create(item_type, item_data)

    def list_by_type_alphabetically(self):
        items = self._item_repository.list_items()
        return sorted(items, key=lambda item: (item[0], item[2]))

    def delete_item(self, item_id):
        return self._item_repository.delete_item(item_id)

    def save(self):
        self._item_repository.save()

ITEM_SERVICE = ItemService()
