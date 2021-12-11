class StubItemService:
    def __init__(self, item_repository):
        self._item_repository = item_repository

    def create_item(self, item_type, item_fields):
        item = self._item_repository.create(item_type, item_fields)
        return item

    # def find_all_items(self):
    #     """Returns list of all items first sorted by item type and then by author"""
    #     items = self._item_repository.find_all()
    #     items_sorted = sorted(items, key=lambda item: (item[1], item[2]))

    #     return items_sorted

    def list_by_type_alphabetically(self):
        items = self._item_repository.list_items()
        return sorted(items, key=lambda item: (item[0], item[2]))

    def delete_item(self, item_title):
        self._item_repository.delete_item(item_title)

    def save(self):
        self._item_repository.save()
