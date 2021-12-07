'''Command Factory'''
import sys
from config import CMD_PROMPTS, ADD_MENU
from utilities.utilities import check_year
from services.item_service import ITEM_SERVICE as default_item_service
from entities.book import Book
from entities.video import Video
from entities.blog import Blog

ENTITY_DICT = {"book": Book, "video": Video, "blog": Blog}

class CommandFactory:
    '''Produces choosable commands to UI'''
    def __init__(self, io, item_service=default_item_service):
        self.io = io
        self.item_service = item_service

        self.cmds = {
            "1": Add(self.io, self.item_service),
            "2": List(self.io, self.item_service),
            "3": Search(self.io, self.item_service),
            "4": Modify(self.io, self.item_service),
            "5": Delete(self.io, self.item_service),
            "0": Quit(self.io, self.item_service)
        }

    def get_command(self, command):
        if command in self.cmds:
            return self.cmds[command]

        return Unknown(self.io, self.item_service)

class Menu:
    def __init__(self, io, item_service, cat=None):
        self.io = io
        self.item_service = item_service
        self.cat = cat

        if self.cat is None:
            self.cmds = []
        else:
            self.cmds = CMD_PROMPTS[cat]

    def perform(self):
        item = []
        for cmd in self.cmds:
            item.append(self._add_info(*cmd))

        self.item_service.create_item(self.cat, item)
        self.io.write("\nUusi lukuvinkki lisätty.")

    def _add_info(self, prompt, error_msg):
        adding = True
        while adding:
            info = self.io.read(prompt)
            if not info:
                self.io.write(error_msg)
            else:
                adding = False
        return info

class Add(Menu):
    def __init__(self, io, item_service=default_item_service):
        Menu.__init__(self, io, item_service)

        self.cmds = {
            "6": AddBook(self.io, self.item_service),
            "7": AddVideo(self.io, self.item_service),
            "8": AddBlog(self.io, self.item_service),
            "9": Menu(self.io, self.item_service),
            "0": Quit(self.io, self. item_service)
        }

    def perform(self):
        while True:
            self.io.write(ADD_MENU)
            command = self.io.read("\nValinta: ")
            # if not command in self.cmds:
            #     continue
            # else:
            #     self.cmds[command].perform()
            #     break
            if command in self.cmds:
                self.cmds[command].perform()
                break

class AddBook(Menu):
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service, 'book')

class AddVideo(Menu):
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service, 'video')

class AddBlog(Menu):
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service, 'blog')
        self.item_service = item_service

class List(Menu):
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service)

    def perform(self):
        self.io.write("\nLukuvinkkilista:\n")
        items = self.item_service.find_all_items()
        if items:
            for item in items:
                item_type = item[0]
                item_str = ENTITY_DICT[item[0]](*item[1])
                self.io.write(f"{item_type.capitalize()} - {item_str}")
        else:
            self.io.write("Sovellukseen ei ole tallennettu vinkkejä ):")

class Search(Menu):
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service)

class Modify(Menu):
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service)

class Delete(Menu):
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service)

class Unknown(Menu):
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service)

    def perform(self):
        pass

class Quit(Menu):
    def __init__(self, io, item_service):
        Menu.__init__(self, io, item_service)

    def perform(self):
        self.io.write("Kiitti & moi!")
        sys.exit(0)
