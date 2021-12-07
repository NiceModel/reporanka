import unittest

from entities.book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book('merz', 'meemikirja', '2021')

    def test_init_book_works(self):
        author = self.book.author
        title = self.book.title
        published = self.book.published
        self.assertEqual(
            (author, title, published),
            ('merz', 'meemikirja', '2021')
        )

    def test_returns_book_str(self):
        expected = "merz: meemikirja (2021)"
        actual = str(self.book)
        self.assertEqual(actual, expected)
