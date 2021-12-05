'''Command Factory'''
import sys
from utilities.utilities import check_year

class CommandFactory:
    '''Produces choosable commands to UI'''
    def __init__(self, io, item_service):
        self.io = io
        self.item_service = item_service
        
        self.commands = {
            "1": Add(self.io, item_service),
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


class Add:
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

        #temporary fix for only books
        item_type = "book"
        item_fields = [title, author_firstname, author_lastname, published]

        self.item_service.create_item(item_type, item_fields)
        self.io.write("Uusi lukuvinkki lisätty.")


class List:
    def __init__(self, io, item_service):
        self.io = io
        self.item_service = item_service

    def perform(self):
        self.io.write("\nLukuvinkkilista:\n")
        items = self.item_service.find_all_items()
        if items:
            for item in items:
                self.io.write(item)
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
        self.io.write("Poistetaan vinkki...")

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


