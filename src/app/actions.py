from collections import deque
import re
from typing import Deque

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
        if item:
            item = deque([item.values()])
            item.appendleft(headers)
            self._io.write(item, True)
        elif item == None:
            self._io.write(OUTPUTS["broken input"])
            return
        else:
            item = []
            self._io.write(OUTPUTS["empty item"])
            return
        
        return item
        

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
            if choice.upper() == YES:
                self._item_service.delete_item(item)
                self._io.write(OUTPUTS['deleting'])
                return
            elif choice.upper() == NO:
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

class Search(Action):

    def __init__(self, io, item_service):
        super().__init__(io, item_service, 'search')

    def perform(self):
        self._io.write(OUTPUTS['search help'])
        items = self._item_service.list_by_type_alphabetically()
        headers = ['type', 'id', 'creator', 'title']
        
        if items:
            results = self._search(items)
            if results:
                self._io.write(OUTPUTS['search results'])
                results.appendleft(headers)
                self._io.write(results, True)
            else:
                self._io.write(OUTPUTS['item not found'])
        else:
            self._io.write(OUTPUTS["empty list"])

        return True

    def _search(self, items):
        results = deque()

        prompt, error_msg = self._cmds[0]
        search_word = str(self._get_info(prompt, error_msg))
        for item in items:
            result = re.findall(search_word, str(item[2:]), re.IGNORECASE)
            if result:
                results.append(item)

        return results


class Quit(Action):
    def __init__(self, io, item_service):
        super().__init__(io, item_service)

    def perform(self):
        self._io.write(OUTPUTS['quit'])
        return False
