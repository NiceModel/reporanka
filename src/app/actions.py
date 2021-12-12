from collections import deque

from config import CMD_PROMPTS, OUTPUTS, YES, NO

class Action:
    '''Superclass for menu actions'''
    def __init__(self, io, item_service, action=None):
        self._io = io
        self._item_service = item_service

        if action is None:
            self._cmds = []
        else:
            self._cmds = CMD_PROMPTS[action]

    def perform(self):
        self._io.write(OUTPUTS['unknown command'])
        return True

    def _get_info(self, prompt, error_msg):
        """Internal method to read and write info from/to the console."""
        adding = True
        while adding:
            info = self._io.read(prompt)
            if not info:
                self._io.write(error_msg)
            else:
                adding = False
        return info

    def _list(self):
        headers = ['type', 'id', 'creator', 'title']
        items = deque(self._item_service.list_by_type_alphabetically())
        
        if items:
            ids = [item[1] for item in items]
            items.appendleft(headers)
            self._io.write(items, True)
        else:
            ids = []
            self._io.write(OUTPUTS["empty list"])

        return ids

    def _show_item_info(self, item):
        headers = ['type', 'creator', 'name', 'published', 'id']
        item = deque([item.values()])
        if item:
            item.appendleft(headers)
        else:
            item = []
            self._io.write(OUTPUTS["empty item"])
        self._io.write(item, True)
        return True
        

class Add(Action):
    '''Superclass for add actions'''
    def __init__(self, io, item_service, action):
        super().__init__(io, item_service, action)
        self._action = action

    def perform(self):
        item = []
        for cmd in self._cmds:
            item.append(self._get_info(*cmd))

        added = self._item_service.create_item(self._action, item)
        if not added:
            self._io.write(OUTPUTS["already in list"])
        else:
            self._io.write(OUTPUTS["added"])
        return True

class AddBook(Add):
    def __init__(self, io, item_service):
        super().__init__(io, item_service, 'book')

class AddBlog(Add):
    def __init__(self, io, item_service):
        super().__init__(io, item_service, 'blog')

class AddVideo(Add):
    def __init__(self, io, item_service):
        super().__init__(io, item_service, 'video')

class List(Action):
    def __init__(self, io, item_service):
        super().__init__(io, item_service)

    def perform(self):
        self._io.write(OUTPUTS['list'])
        self._list()
        return True

class Delete(Action):
    """Menu subclass for deleting an item."""
    def __init__(self, io, item_service):
        super().__init__(io, item_service, 'delete')

    def perform(self):
        self._io.write(OUTPUTS['list'])
        items = self._list()

        if items:
            prompt, error_msg = self._cmds[0]
            item = self._get_info(prompt, error_msg)
            if item not in items:
                self._io.write(OUTPUTS['item not found'])
            else:
                self._delete_item(item, items)

        return True

    def _delete_item(self, item, items):
        for i in range(len(items)):
            if items[i] == item:
                self._confirm(item)

    def _confirm(self, item):
        while True:
            choice = self._io.read(OUTPUTS['confirm'])
            if choice == YES:
                self._item_service.delete_item(item)
                self._io.write(OUTPUTS['deleting'])
                return
            elif choice == NO:
                self._io.write(OUTPUTS['not deleted'])
                return
class Details(Action):
    def __init__(self, io, item_service):
         super().__init__(io, item_service, 'details')

    def perform(self):
        items = self._list()
        found_item = None
        if items:
            prompt, error_msg = self._cmds[0]
            _id = self._get_info(prompt, error_msg)
            if _id not in items:
                self._io.write(OUTPUTS['item not found'])
            else:
                found_item = self._item_service.find_by_id(_id)
        self._show_item_info(found_item)
        return True

class Quit(Action):
    def __init__(self, io, item_service):
        super().__init__(io, item_service)

    def perform(self):
        self._io.write(OUTPUTS['quit'])
        return False
