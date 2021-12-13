"""Module for an item service to connect an item repository to the application."""
from repositories.item_repository import (
    ITEM_REPOSITORY as default_item_repository
)

class ItemService:
    """Class for item service.

    attr:
        item_repository: ItemRepository: repository object where the books are stored
    """
    def __init__(self, item_repository=default_item_repository):
        self._item_repository = item_repository

    def create_item(self, item_type, item_data):
        '''Creates a new item.

        args:
            item_type: str: type of the item (book/blog/video)
            item_data: list: item's information
        return:
            bool: True if item is created, otherwise False
        '''
        return self._item_repository.create(item_type, item_data)

    def list_by_type_alphabetically(self):
        '''Lists all items by type (primary) and alphabetically
        by creator's name (secondary).

        return:
            sorted list
        '''
        items = self._item_repository.list_items()
        return sorted(items, key=lambda item: (item[0], item[2]))

    def delete_item(self, item_id):
        '''Deletes an item.

        args:
            item_id: str: identifier of the item
        return:
            Item object if item exists, otherwise None
        '''
        return self._item_repository.delete_item(item_id)

    def save(self):
        '''Saves the item repository ro a csv file.'''
        self._item_repository.save()

    def find_by_id(self, item_id):
        '''Finds an item by its identifier.

        args:
            item_id: str: identifier of the item
        return:
            item details (dict) if item exists, otherwise None'''
        return self._item_repository.find_by_id(item_id)
