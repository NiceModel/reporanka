import unittest

from entities.item import Item, Book, Blog, Video

class TestItem(unittest.TestCase):
    def setUp(self):
        self.cat = "item"
        self.item_id = "0000"
        self.creator = "Pablo Picasso"
        self.title = "Les Demoiselles d'Avignon"
        self.published = "1907"
        self.item = Item(self.creator, self.title, self.published, self.item_id)

    def test_generates_random_id(self):
        item = Item(self.creator, self.title, self.published, None)
        actual = item.item_id
        self.assertNotEqual(actual, self.item_id)

    def test_does_not_generate_random_id(self):
        item = self.item
        actual = item.item_id
        self.assertEqual(actual, self.item_id)

    def test_info_property(self):
        expected = [self.cat, self.item_id, self.creator, self.title]
        actual = self.item.info
        self.assertEqual(actual, expected)

    def test_details_property(self):
        expected = {
            'type': self.cat, 'creator': self.creator,
            'title': self.title, 'published': self.published, 'id': self.item_id
        }
        actual = self.item.details
        self.assertEqual(actual, expected)

    def test_csv_data_property(self):
        expected = f"{self.cat};{self.creator};{self.title};{self.published};{self.item_id}"
        actual = self.item.csv_data
        self.assertEqual(actual, expected)

class TestBook(unittest.TestCase):
    def setUp(self):
        self.cat = "book"
        self.item_id = "0000"
        self.author = "Patrick Ness"
        self.title = "The Knife of Never Letting Go"
        self.published = "2008"
        self.book = Book(self.author, self.title, self.published, self.item_id)

    def test_book_details(self):
        expected = {
            'type': self.cat, 'author': self.author,
            'name': self.title, 'published': self.published, 'id': self.item_id
        }
        actual = self.book.details
        self.assertEqual(actual, expected)

    def test_csv_data_property(self):
        expected = f"{self.cat};{self.author};{self.title};{self.published};{self.item_id}"
        actual = self.book.csv_data
        self.assertEqual(actual, expected)

class TestBlog(unittest.TestCase):
    def setUp(self):
        self.cat = "blog"
        self.item_id = "0000"
        self.creator = "Eero Tarmo"
        self.name = "Soundi.fi"
        self.title = "Androgyyniä laulua ja irtonaista kävelyä – tältä kuulostaa Arto Tuunelan kevät"
        self.url = "https://www.soundi.fi/jutut/pariisin-kevat-nokkamies-kasasi-kevat-aiheisen-soittolistan/"
        self.published = "13.3.2016"
        self.blog = Blog(self.creator, self.name, self.title, self.url, self.published, self.item_id)

    def test_blog_details(self):
        expected = {
            'type': self.cat, 'creator': self.creator,
            'blog': self.name, 'post': self.title,
            'url': self.url, 'published': self.published, 'id': self.item_id
        }
        actual = self.blog.details
        self.assertEqual(actual, expected)

    def test_csv_data_property(self):
        expected = f"{self.cat};{self.creator};{self.name};{self.title};{self.url};{self.published};{self.item_id}"
        actual = self.blog.csv_data
        self.assertEqual(actual, expected)

class TestVideo(unittest.TestCase):
    def setUp(self):
        self.cat = "video"
        self.item_id = "0000"
        self.creator = "Christian Duenas"
        self.title = "Pygame Menu System Tutorial Part 2: Building the Menu and States"
        self.url = "https://youtu.be/bmRFi7-gy5Y"
        self.published = "24.7.2020"
        self.video = Video(self.creator, self.title, self.url, self.published, self.item_id)

    def test_blog_details(self):
        expected = {
            'type': self.cat, 'creator': self.creator, 'name': self.title,
            'url': self.url, 'published': self.published, 'id': self.item_id
        }
        actual = self.video.details
        self.assertEqual(actual, expected)

    def test_csv_data_property(self):
        expected = f"{self.cat};{self.creator};{self.title};{self.url};{self.published};{self.item_id}"
        actual = self.video.csv_data
        self.assertEqual(actual, expected)
