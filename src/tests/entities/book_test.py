import unittest

from entities.book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book('Meemikirja', 'Meri', "Siili", '2021')

    def test_init_book_works(self):
        author_firstname = self.book.author_firstname
        author_lastname = self.book.author_lastname
        title = self.book.title
        published = self.book.published
        self.assertEqual(
            (author_firstname, author_lastname, title, published),
            ("Meri", "Siili", "Meemikirja", "2021")
        )

    def test_returns_book_str(self):
        expected = "Meri Siili: Meemikirja (2021)"
        actual = str(self.book)
        self.assertEqual(actual, expected)
