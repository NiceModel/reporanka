'''Command Factory'''
import sys
from config import CMD_PROMPTS, ADD_MENU
from services.item_service import ITEM_SERVICE as default_item_service
from entities.book import Book
from entities.video import Video
from entities.blog import Blog

ENTITY_DICT = {"book": Book, "video": Video, "blog": Blog}

class CommandFactory:
    '''Produces choosable commands to UI

    attr:
        io: console io for interacting with the user
        item_service: service for interacting with reading tip items
    '''
    def __init__(self, io, item_service=default_item_service):
        self.io = io
        self.item_service = item_service

        self.cmds = {
            "1": Add(self.io, self.item_service),
            "2": List(self.io, self.item_service),
            "3": Delete(self.io, self.item_service),
            "4": Search(self.io, self.item_service),
            "5": Modify(self.io, self.item_service),
            "0": Quit(self.io, self.item_service)
        }

    def get_command(self, command):
        """Returns the command the user has chosen from predefined inputs."""
        if command in self.cmds:
            return self.cmds[command]

        return Unknown(self.io, self.item_service)

class Menu:
    """Superclass for menu actions.

    attr:
        io: module for reading/writing inputs/outputs
        item_service: service for interacting with reading tip items
        cat: str: specifies the category of a reading tip item
        cmds: list: prompts for user input, specific to item category
    """
    def __init__(self, io, item_service, cat=None):
        self.io = io
        self.item_service = item_service
        self.cat = cat

        if self.cat is None:
            self.cmds = []
        else:
            self.cmds = CMD_PROMPTS[cat]

    def perform(self):
        """Performs the chosen action."""
        item = []
        for cmd in self.cmds:
            item.append(self._add_info(*cmd))

        added = self.item_service.create_item(self.cat, item)
        if added == "duplicate":
            self.io.write("\nLukuvinkki on jo tallennettu aiemmin!")
        else:
            self.io.write("\nUusi lukuvinkki lisätty.")
        return True

    def _add_info(self, prompt, error_msg):
        """Internal method to read and write info from/to the console."""
        adding = True
        while adding:
            info = self.io.read(prompt)
            if not info:
                self.io.write(error_msg)
            else:
                adding = False
        return info

class Add(Menu):
    """Menu subclass for adding different types of reading tip items."""
    def __init__(self, io, item_service=default_item_service):
        Menu.__init__(self, io, item_service)

        self.cmds = {
            "1": AddBook(self.io, self.item_service),
            "2": AddVideo(self.io, self.item_service),
            "3": AddBlog(self.io, self.item_service),
            "4": MainMenu(self.io, self.item_service),
            "0": Quit(self.io, self. item_service)
        }

    def perform(self):
        """Method to let the user choose the item to be added."""
        while True:
            self.io.write(ADD_MENU)
            command = self.io.read("\nValinta: ")
            if command in self.cmds:
                self.cmds[command].perform()
                return True

class AddBook(Menu):
    """Menu subclass for adding books."""
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service, 'book')

class AddVideo(Menu):
    """Menu subclass for adding videos."""
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service, 'video')

class AddBlog(Menu):
    """Menu subclass for adding blog posts."""
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service, 'blog')
        self.item_service = item_service

class List(Menu):
    """Menu subclass for listing the reading tips."""
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service)

    def perform(self):
        """Finds the reading tips and prints them to console."""
        self.io.write("\nLukuvinkkilista:\n")
        items = self.item_service.find_all_items()
        if items:
            for item in items:
                item_type = item[0]
                try:
                    item_str = ENTITY_DICT[item[0]](*item[1])
                    self.io.write(f"{item_type.capitalize()} - {item_str}")
                except TypeError:
                    pass
                except KeyError:
                    pass
        else:
            self.io.write("Sovellukseen ei ole tallennettu vinkkejä :(")
        return True

class Search(Menu):
    """Menu subclass for searching specific items."""
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service)

class MainMenu(Menu):
    """Menu subclass for an unknown user input."""
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service)

    def perform(self):
        """Does nothing if the app does not recognise a command."""
        return True

class Modify(Menu):
    """Menu subclass for modifying an item's data."""
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service)

class Delete(Menu):
    """Menu subclass for deleting an item."""
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service, 'delete')

    def _delete_item(self):
        """Internal method to read and write info from/to the console."""
        prompt, error_msg = self.cmds[0]
        deleting = True
        while deleting:
            info = self.io.read(prompt)
            if not info:
                self.io.write(error_msg)
            else:
                deleting = False
        return info

    def perform(self):
        items = self.item_service.find_all_items()
        titles = []
        if items:
            self.io.write("Vinkit:")
            for item in items:
                item_type = item[0]
                try:
                    item_str = ENTITY_DICT[item[0]](*item[1])
                    self.io.write(f"{item_type.capitalize()} - {item_str}")
                    titles.append(item_str.title)
                except TypeError:
                    pass
                except KeyError:
                    pass
        else:
            self.io.write("Sovellukseen ei ole tallennettu vinkkejä :(")

        deleted = self._delete_item()

        if deleted not in titles:
            self.io.write('Teosta ei löytynyt.')
        else:
            for i in range(len(titles)):
                if titles[i] == deleted:
                    response = self.io.read("\nOletko varma? K/E ")

                    if response == "K":
                        self.item_service.delete_item(deleted)
                        self.io.write("Poistetaan vinkki...")
                    else:
                        pass
        return True

class Unknown(Menu):
    """Menu subclass for an unknown user input."""
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service)

    def perform(self):
        """Does nothing if the app does not recognise a command."""
        self.io.write('Komentoa ei löytynyt, yritä uudelleen.')
        return True

class Quit(Menu):
    """Menu subclass for quitting the application."""
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service)

    def perform(self):
        """Quits the application."""
        self.io.write("Kiitti & moi!")
        # sys.exit(0)
        return False
