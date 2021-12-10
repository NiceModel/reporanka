class StubItemService:
    def __init__(self, item_repository):
        self._item_repository = item_repository

    def create_item(self, item_type, item_fields):
        item_id = '0000'
        item = self._item_repository.create(
            item_id,
            item_type,
            item_fields
        )
        return item

    def find_all_items(self):
        """Returns list of all items first sorted by item type and then by author"""
        items = self._item_repository.find_all()
        items_sorted = sorted(items, key=lambda item: (item[1], item[2]))

        return items_sorted

    def delete_item(self, item_title):
        self._item_repository.delete_item(item_title)
