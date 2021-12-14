'''Module for executable menu.'''
from collections import deque
import re
import webbrowser

from config import CMD_PROMPTS, OUTPUTS, YES, NO, HEADERS

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
        """Performs the action and returns a boolean value
        depending on whether the app should be running after
        execution.
        """
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
        """Writes all items to the console, tabulated.
        Truncates over 20 character long fields.

        return:
            ids: list: list of item ids
        """
        items = self._item_service.list_by_type_alphabetically()

        if items:
            items = deque([
                [field if len(field) <= 20 else f"{field[:20]}..." for field in item]
                for item in items])
            ids = [item[1] for item in items]
            items.appendleft(HEADERS)
            self._io.write(items, True)
        else:
            ids = []
            self._io.write(OUTPUTS["empty list"])

        return ids

    def _show_details(self, item):
        """Prints detailed info of an item.
        Open url of an item in a new browser tab.
        """
        if item:
            info = [[key, val] for key, val in item.items()]
            self._io.write(info, True)

            url = ''
            if info[0][1] == 'blog':
                if 'http' not in info[4][1]:
                    url = 'https://' + info[4][1]
                else:
                    url = info[4][1]
                webbrowser.open(url)

            if info[0][1] == 'video':
                if 'http' not in info[3][1]:
                    url = 'https://' + info[3][1]
                else:
                    url = info[3][1]
                webbrowser.open(url)

        else:
            self._io.write(OUTPUTS['broken input'])

class Add(Action):
    '''Superclass for add actions'''
    def __init__(self, io, item_service, action):
        super().__init__(io, item_service, action)
        self._action = action

    def perform(self):
        '''Adds an item based on user input.'''
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
    '''Subclass for adding books.'''
    def __init__(self, io, item_service):
        super().__init__(io, item_service, 'book')

class AddBlog(Add):
    '''Subclass for adding blog posts.'''
    def __init__(self, io, item_service):
        super().__init__(io, item_service, 'blog')

class AddVideo(Add):
    '''Subclass for adding videos.'''
    def __init__(self, io, item_service):
        super().__init__(io, item_service, 'video')

class List(Action):
    '''Action for listing item information.'''
    def __init__(self, io, item_service):
        super().__init__(io, item_service)

    def perform(self):
        '''Performs the action.'''
        self._io.write(OUTPUTS['list'])
        self._list()
        return True

class Delete(Action):
    """Action for deleting an item."""
    def __init__(self, io, item_service):
        super().__init__(io, item_service, 'delete')

    def perform(self):
        '''Performs the delete action.'''
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
        '''Deletes an item.

        args:
            item: str: identifier for an item
            items: list: list of items currently in the repository.
        '''
        for i in range(len(items)):
            if items[i] == item:
                self._confirm(item)

    def _confirm(self, item):
        '''Confirms the deletion of the item.'''
        while True:
            choice = self._io.read(OUTPUTS['confirm'])
            if choice.upper() == YES:
                self._item_service.delete_item(item)
                self._io.write(OUTPUTS['deleting'])
                return
            if choice.upper() == NO:
                self._io.write(OUTPUTS['not deleted'])
                return

class Clear(Action):
    '''Action for clearing all items and creating an empty document.'''
    def __init__(self, io, item_service):
        super().__init__(io, item_service, 'clear')

    def perform(self):
        '''Confirms the clear action.'''
        self._io.write(OUTPUTS['list'])

        choice = self._io.read(OUTPUTS['confirm_clearing'])
        if choice.upper() == YES:
            self._item_service.clear()
            self._io.write(OUTPUTS['clearing'])
        elif choice.upper() == NO:
            self._io.write(OUTPUTS['not cleared'])
        else:
            self._io.write(OUTPUTS['unknown command'])
        return True

class Details(Action):
    '''Action for showing the details of an item.'''
    def __init__(self, io, item_service):
        super().__init__(io, item_service, 'details')

    def perform(self):
        '''Lists all items and then fetches the details.'''
        ids = self._list()
        found_item = None
        if ids:
            prompt, error_msg = self._cmds[0]
            item_id = self._get_info(prompt, error_msg)
            if item_id not in ids:
                self._io.write(OUTPUTS['item not found'])
            else:
                found_item = self._item_service.find_by_id(item_id)
                self._io.write(OUTPUTS['details results'])
                self._show_details(found_item)
        return True

class Search(Action):
    '''Action for searching specific items.'''
    def __init__(self, io, item_service):
        super().__init__(io, item_service, 'search')

    def perform(self):
        '''Performs a search with a search word provided by the user.'''
        self._io.write(OUTPUTS['search help'])
        items = self._item_service.list_by_type_alphabetically()

        if items:
            results = self._search(items)
            if results:
                self._io.write(OUTPUTS['search results'])
                results = deque([
                    [field if len(field) <= 20 else f"{field[:20]}..." for field in item]
                    for item in results])
                results.appendleft(HEADERS)
                self._io.write(results, True)
            else:
                self._io.write(OUTPUTS['item not found'])
        else:
            self._io.write(OUTPUTS["empty list"])

        return True

    def _search(self, items):
        '''Internal method for performing a search.'''
        results = deque()

        prompt, error_msg = self._cmds[0]
        search_word = str(self._get_info(prompt, error_msg))
        for item in items:
            result = re.findall(search_word, str(item[2:]), re.IGNORECASE)
            if result:
                results.append(item)

        return results


class Quit(Action):
    '''Action for quitting the application.'''
    def __init__(self, io, item_service):
        super().__init__(io, item_service)

    def perform(self):
        '''Quits the application.'''
        self._io.write(OUTPUTS['quit'])
        return False
