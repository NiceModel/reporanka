"""Basic functionality"""

# from utilities.utilities import check_year
from config import TITLE
# from app.command_factory import CommandFactory
from app.menu import MainMenu, AddMenu

class App:
    """Handles the UI functionality for the application"""
    def __init__(self, item_service, io):
        # self._item_service = item_service
        self._io = io
        # self._commands = CommandFactory(io, item_service)
        self.running = False
        self.menu = 'main'
        self._main_menu = MainMenu(io, item_service)
        self._add_menu = AddMenu(io, item_service)

    # def run(self):
    #     """Starts the application."""
    #     self.running = True
    #     self.io.write("\nLUKUVINKKIKIRJASTO")
    #     while self.running:
    #         self.io.write(INSTRUCTIONS)
    #         command = self.io.read("Komento: ")
    #         self.running = self.commands.get_command(command).perform()

    def run(self):
        self.running = True
        self._io.write(TITLE)
        while self.running:
            if self.menu == 'main':
                self.running, self.menu = self._main_menu.display()
            elif self.menu == 'add':
                self.running, self.menu = self._add_menu.display()

