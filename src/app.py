"""Basic functionality"""

from command_factory import CommandFactory


class App:
    """Handles the UI functionality for the application"""
    def __init__(self, book_service, io):
        self.book_service = book_service
        self.io = io
        self.commands = CommandFactory(io, book_service)
        self.running = False    

    def run(self):
        """Handles running the application"""
        self.running = True
        self.io.write("\nLUKUVINKKIKIRJASTO")

        while self.running:
            self.io.guide()
            command = self.io.read("Komento: ")
            self.commands.get_command(command).perform()
