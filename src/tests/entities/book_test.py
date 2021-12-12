import unittest

from entities.item import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.author = 'Naomi Klein'
        self.title = 'No Logo'
        self.published = '1999'
        self.item_id = "3c4d"
        self.book = Book(self.author, self.title, self.published, self.item_id)

    def test_init_book(self):
        self.assertEqual(
            (self.author, self.title, self.published),
            ('Naomi Klein', 'No Logo', '1999')
        )

    def test_returns_book_str(self):
        expected = "Naomi Klein: No Logo (1999)"
        actual = str(self.book)
        self.assertEqual(actual, expected)