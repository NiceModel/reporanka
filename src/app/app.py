"""Basic functionality"""
from config import TITLE
from app.menu import Menu

class App:
    """Handles the UI functionality for the application
    args:
        io: handles the user inputs and app outputs
        item_service: service for interacting with the item library

    attr:
        running: bool: True if app is currently running, otherwise false
        menu: str: current menu to be displayed
        main_menu: Menu: a menu object for the main menu
        add_menu: Menu: a menu object for adding items
    """
    def __init__(self, item_service, io):
        self._item_service = item_service
        self._io = io
        self.running = False
        self.menu = 'main'
        self._main_menu = Menu(io, item_service)
        self._add_menu = Menu(io, item_service, 'add')

    def run(self):
        """Starts the application and runs until the user chooses to quit.
        Saves item repository to a csv file before quitting.
        """
        self.running = True
        self._io.write(TITLE)
        while self.running:
            if self.menu == 'main':
                self.running, self.menu = self._main_menu.display()
            elif self.menu == 'add':
                self.running, self.menu = self._add_menu.display()
        self._item_service.save()
