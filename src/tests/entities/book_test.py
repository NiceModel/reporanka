import unittest

from entities.item import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book('Naomi Klein', 'No Logo', '1999')

    def test_init_book_works(self):
        author = self.book.author
        title = self.book.title
        published = self.book.published
        self.assertEqual(
            (author, title, published),
            ('Naomi Klein', 'No Logo', '1999')
        )

    def test_returns_book_str(self):
        expected = "Naomi Klein: No Logo (1999)"
        actual = str(self.book)
        self.assertEqual(actual, expected)

    def test_book_short_string(self):
        expected = 'Naomi Klein: No Logo'
        self.assertEqual(self.book.short_str, expected)
