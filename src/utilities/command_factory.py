'''Command Factory'''
import sys
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
        
        self.commands = {
            "1": Add(self.io),
            "2": List(self.io, self.item_service),
            "3": Search(self.io, self.item_service),
            "4": Modify(self.io, self.item_service),
            "5": Delete(self.io, self.item_service),
            "0": Quit(self.io)
        }

    def get_command(self, command):
        if command in self.commands:
            return self.commands[command]

        return Unknown(self.io)

class Menu:
    def __init__(self, io):
        self.io = io

    def perform(self):
        pass

class Add:
    def __init__(self, io, item_service=default_item_service):
        self.io = io
        self.item_service = item_service

        self.commands = {
            "6": AddBook(self.io, self.item_service),
            "7": AddVideo(self.io, self.item_service),
            "8": AddBlog(self.io, self.item_service),
            "9": Menu(self.io),
            "0": Quit(self.io)
        }

    def perform(self):
        while True:
            self.io.add_menu()
            command = self.io.read("\nValinta: ")
            if not command in self.commands:
                continue
            else:
                self.commands[command].perform()
                break

class AddBook:
    def __init__(self, io, item_service):
        self.io = io
        self.item_service = item_service

    def perform(self):

        authors = []
        while True:
            author_firstname = self.io.read("Kirjailijan etunimi: ")
            while not author_firstname:
                self.io.write("Kirjailijan etunimi on lisättävä!")
                author_firstname = self.io.read("Kirjailijan etunimi: ")

            author_lastname = self.io.read("Kirjailijan sukunimi: ")
            while not author_lastname:
                self.io.write("Kirjailijan sukunimi on lisättävä!")
                author_lastname = self.io.read("Kirjailijan sukunimi: ")

            authors.append((author_lastname, author_firstname))
            
            new_author = self.io.read("Lisää uusi kirjailija? Kyllä: Paina jotain merkkiä + Enter. Ei: Enter\n")
            if not new_author:
                break
            else:
                continue

        title = self.io.read("Kirjan nimi: ")
        while not title:
            self.io.write("Kirjan nimi on lisättävä!")
            title = self.io.read("Kirjan nimi: ")

        check = True
        while check:
            published = self.io.read("Julkaisuvuosi: ")
            if not check_year(published):
                self.io.write("Julkaisuvuosi ei ole kelvollinen!")
            else:
                check = False

        item_type = "book"
        item_fields = [title, author_firstname, author_lastname, published]

        self.item_service.create_item(item_type, item_fields)
        self.io.write("\nUusi lukuvinkki lisätty.")

class AddVideo:
    def __init__(self, io, item_service):
        self.io = io
        self.item_service = item_service

    def perform(self):

        title = self.io.read("Videon nimi: ")
        while not title:
            self.io.write("Videon nimi on lisättävä!")
            title = self.io.read("Videon nimi: ")

        address = self.io.read("Videon osoite: ")
        while not address:
            self.io.write("Videon osoite on lisättävä!")
            address = self.io.read("Videon osoite: ")

        creator = self.io.read("Videon tekijä: ")
        while not creator:
            self.io.write("Videon tekijä on lisättävä!")
            creator = self.io.read("Videon tekijä: ")

        published = self.io.read("Videon julkaisupäivä: ")
        while not creator:
            self.io.write("Videon julkaisupäivä on lisättävä!")
            published = self.io.read("Videon julkaisupäivä: ")
        
        item_type = "video"
        item_fields = [title, address, creator, published]

        self.item_service.create_item(item_type, item_fields)
        self.io.write("\nUusi lukuvinkki lisätty.")

class AddBlog:
    def __init__(self, io, item_service):
        self.io = io
        self.item_service = item_service

    def perform(self):

        name = self.io.read("Blogin nimi: ")
        while not name:
            self.io.write("Blogin nimi on lisättävä!")
            name = self.io.read("Blogin nimi: ")

        post = self.io.read("Postaus: ")
        while not post:
            self.io.write("Postauksen nimi on lisättävä!")
            post= self.io.read("Postaus: ")

        address = self.io.read("Blogin osoite: ")
        while not address:
            self.io.write("Blogin osoite on lisättävä!")
            address = self.io.read("Blogin osoite: ")

        blogger = self.io.read("Blogin kirjoittaja: ")
        while not blogger:
            self.io.write("Blogin kirjoittaja on lisättävä!")
            blogger = self.io.read("Blogin kirjoittaja ")

        published = self.io.read("Postauksen julkaisupäivä: ")
        while not published:
            self.io.write("Postauksen julkaisupäivä on lisättävä!")
            published = self.io.read("Postauksen julkaisupäivä: ")

        item_type = "blog"
        item_fields = [name, post, blogger, address, published]

        self.item_service.create_item(item_type, item_fields)
        self.io.write("\nUusi lukuvinkki lisätty.")

class List:
    def __init__(self, io, item_service):
        self.io = io
        self.item_service = item_service

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

class Search:
    def __init__(self, io, item_service):
        self.io = io
        self.item_service = item_service

    # TODO: Lisää tänne varsinaiset metodit
    def perform(self):
        self.io.write("Haetaan vinkkiä...")

class Modify:
    def __init__(self, io, item_service):
        self.io = io
        self.item_service = item_service

    # TODO: Lisää tänne varsinaiset metodit
    def perform(self):
        self.io.write("Muokataan vinkkiä...")

class Delete:
    def __init__(self, io, item_service):
        self.io = io
        self.item_service = item_service

    # TODO: Lisää tänne varsinaiset metodit
    def perform(self):
        items = self.item_service.find_all_items()
        self.io.write("Anna poistettavan teoksen nimi...")
        item_title = self.io.read("Nimi: ")

        while not item_title:
            self.io.write("Teoksen nimi on annettava!")
            item_title = self.io.read("Nimi: ")

        for item in items:
            if str(item[1][0]) == item_title:
                found_item = item
                print(found_item)
                self.item_service.delete_item(item_title)

                self.io.write("Poistetaan vinkki...")
            else:
                print("Teosta ei löytynyt")
                break

class Unknown:
    def __init__(self, io):
        self.io = io

    def perform(self):
        pass

class Quit:
    def __init__(self, io):
        self.io = io

    def perform(self):
        self.io.write("Kiitti & moi!")
        sys.exit(0)


