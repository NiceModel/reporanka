'''Command Factory'''
import sys
from utilities import check_year
from services.book_service import (book_service as default_book_service)


class CommandFactory:
    '''Produces choosable commands to UI'''
    def __init__(self, io, book_service):
        self.io = io
        self.book_service = book_service
        
        self.commands = {
            "1": Add(self.io, book_service),
            "2": List(self.io, self.book_service),
            "3": Search(self.io, self.book_service),
            "4": Modify(self.io, self.book_service),
            "5": Delete(self.io, self.book_service),
            "0": Quit(self.io)
        }

    def get_command(self, command):
        if command in self.commands:
            return self.commands[command]

        return Unknown(self.io)


class Add:
    def __init__(self, io, book_service):
        self.io = io
        self.book_service = book_service

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

        self.book_service.create_book(authors, title, published)
        self.io.write("Uusi lukuvinkki lisätty.")


class List:
    def __init__(self, io, book_service):
        self.io = io
        self.book_service = book_service

    def perform(self):
        self.io.write("\nLukuvinkkilista:\n")
        books = self.book_service.find_all_books()
        if books:
            for book in books:
                self.io.write(book)
        else:
            self.io.write("Sovellukseen ei ole tallennettu vinkkejä ):")

class Search:
    def __init__(self, io, book_service):
        self.io = io
        self.book_service = book_service

    # TODO: Lisää tänne varsinaiset metodit
    def perform(self):
        self.io.write("Haetaan vinkkiä...")

class Modify:
    def __init__(self, io, book_service):
        self.io = io
        self.book_service = book_service

    # TODO: Lisää tänne varsinaiset metodit
    def perform(self):
        self.io.write("Muokataan vinkkiä...")

class Delete:
    def __init__(self, io, book_service):
        self.io = io
        self.book_service = book_service

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


