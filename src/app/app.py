"""Basic functionality"""

# from utilities.utilities import check_year
from config import INSTRUCTIONS
from utilities.command_factory import CommandFactory

class App:
    """Handles the UI functionality for the application"""
    def __init__(self, item_service, io):
        self.item_service = item_service
        self.io = io
        self.commands = CommandFactory(io, item_service)
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.io.guide()
            command = self.io.read("Komento: ")
            self.commands.get_command(command).perform()
