import unittest
from config import INSTRUCTIONS
from collections import deque
from app.app import App

"""
class StubIO:
    def __init__(self):
        self.authors = deque(["", "Meri"])
        self.titles = deque(["", "Meemikirja"])
        self.years = deque(["", "2021"])
        self.features = deque(["1", "2", "0"])

        self.values = []

    def write(self, value):
        self.values.append(value)
        return value

    def read(self, prompt):
        instructions = INSTRUCTIONS
        author = "Kirjailija: "
        title = "Nimi: "
        published = "Julkaisuvuosi: "

        if prompt == instructions:
            return self.features.popleft()
        elif prompt == author:
            return self.authors.popleft()
        elif prompt == title:
            return self.titles.popleft()
        elif prompt == published:
            return self.years.popleft()


class StubBookService:
    def __init__(self):
        self.item_list = ["kirja1", "kirja2"]

    def create_book(self, author, title, published):
        return f"{author}: {title} ({published})"

    def find_all_books(self):
        return self.book_list


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App(StubBookService(), StubIO())

    def test_add_book(self):
        self.app._add_book()
        expected = [
            "Lisätään lukuvinkki...",
            "Kirjailijan nimi on lisättävä!",
            "Kirjan nimi on lisättävä!",
            "Julkaisuvuosi ei ole kelvollinen!",
            "\nUusi lukuvinkki 'Meri: Meemikirja (2021)' lisätty."
        ]
        self.assertEqual(self.app.io.values, expected)

    def test_list_books_not_empty(self):
        self.app._list_books()
        expected = ["Listataan lukuvinkit...", "kirja1", "kirja2"]
        self.assertEqual(self.app.io.values, expected)

    def test_list_books_empty(self):
        self.app.book_service.book_list = []
        self.app._list_books()
        expected = [
            "Listataan lukuvinkit...",
            "Sovellukseen ei ole tallennettu vinkkejä ):"
        ]
        self.assertEqual(self.app.io.values, expected)

    def test_main_loop(self):
        self.app.run()
        self.assertFalse(self.app.running)
"""