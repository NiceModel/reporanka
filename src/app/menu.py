'''Module for menu objects.'''
from config import OUTPUTS, INSTRUCTIONS, ADD_MENU
from app.actions import (
    Action, AddBook, AddBlog, AddVideo,
    List, Delete, Quit, Details, Search
)

class Menu:
    '''A class for menus.

    args:
        io: io for user inputs/console outputs
        item_service: service for interacting with the item library
        name: str: name of the menu; defaults to 'main'
    attr:
        cmds: dict: commands choosable from the menu
        instructions: str: instructions for choosing menu commands
        unknown: Action: placeholder action for unrecognised commands
    '''
    def __init__(self, io, item_service, name='main'):
        self._io = io
        self._name = name
        self._unknown = Action(io, item_service)
        self._setup(item_service)

    def _setup(self, item_service):
        if self._name == 'main':
            self._instructions = INSTRUCTIONS
            self._cmds = {
                "1": "add",
                "2": List(self._io, item_service),
                "3": Delete(self._io, item_service),
                "4": Details(self._io, item_service),
                "5": Search(self._io, item_service),
                # "6": Modify(self.io, self.item_service),
                "0": Quit(self._io, item_service)
            }
        elif self._name == 'add':
            self._instructions = ADD_MENU
            self._cmds = {
                "1": AddBook(self._io, item_service),
                "2": AddVideo(self._io, item_service),
                "3": AddBlog(self._io, item_service),
                "4": "main",
                "0": Quit(self._io, item_service)
            }

    def display(self):
        '''Displays the current menu in console.

        return:
            running: bool: True if application is still running, otherwise false
            menu: str: next menu to be displayed
        '''
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
        '''Internal method for fetching next executable command. Return unknown if
        command is not found.
        '''
        if command in self._cmds:
            return self._cmds[command]
        return self._unknown

    def _is_action(self, action):
        '''Internal method for checking whether the action is Action or Menu.'''
        if isinstance(action, Action):
            return True
        return False
