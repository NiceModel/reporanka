from config import OUTPUTS, INSTRUCTIONS, ADD_MENU
from app.actions import (
    Action, AddBook, AddBlog, AddVideo,
    List, Delete, Quit
)

class Menu:
    '''Superclass for menus.'''
    def __init__(self, io, item_service):
        self._io = io
        self._item_service = item_service
        self._cmds = {}
        self._instructions = ''
        self._name = ''
        self._unknown = Action(io, item_service)

    def display(self):
        running = True
        self._io.write(self._instructions)
        command = self._io.read(OUTPUTS['choice'])
        action = self._get_action(command)
        if self._is_action(action):
            running = action.perform()
            menu = self._name if action == self._unknown else 'main'
        else:
            menu = action

        return running, menu

    def _get_action(self, command):
        if command in self._cmds:
            return self._cmds[command]

        return self._unknown

    def _is_action(self, action):
        if isinstance(action, Action):
            return True
        return False

class MainMenu(Menu):
    def __init__(self, io, item_service):
        super().__init__(io, item_service)
        self._instructions = INSTRUCTIONS
        self._name = 'main'
        self._cmds = {
            "1": "add",
            "2": List(self._io, self._item_service),
            "3": Delete(self._io, self._item_service),
            # "4": Search(self.io, self.item_service),
            # "5": Modify(self.io, self.item_service),
            "0": Quit(self._io, self._item_service)
        }

class AddMenu(Menu):
    def __init__(self, io, item_service):
        super().__init__(io, item_service)
        self._instructions = ADD_MENU
        self._name = 'add'
        self._cmds = {
            "1": AddBook(self._io, self._item_service),
            "2": AddVideo(self._io, self._item_service),
            "3": AddBlog(self._io, self._item_service),
            "4": "main",
            "0": Quit(self._io, self._item_service)
        }
