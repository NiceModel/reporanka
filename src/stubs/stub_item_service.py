class StubItemService:
    def __init__(self, item_repository):
        self._item_repository = item_repository

    def create_item(self, item_type, item_fields):
        item = self._item_repository.create(item_type, item_fields)
        return item

    def list_by_type_alphabetically(self):
        items = self._item_repository.list_items()
        return sorted(items, key=lambda item: (item[0], item[2]))

    def delete_item(self, item_title):
        self._item_repository.delete_item(item_title)

    def save(self):
        self._item_repository.save()
