import unittest

from entities.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book('Meri', 'Meemikirja', '2021')

    def test_returns_book_str(self):
        expected = "Meri: Meemikirja (2021)"
        actual = self.book
        self.assertEqual(expected, actual)