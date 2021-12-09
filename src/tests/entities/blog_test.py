import unittest

from entities.blog import Blog

class TestBlog(unittest.TestCase):
    def setUp(self):
        self.blog = Blog("sopuli", "sopulin blogi", "testipostaus", "url", "1.1.2022")

    def test_init_blog(self):
        name = self.blog.name
        post = self.blog.title
        address = self.blog.address
        blogger = self.blog.blogger
        published = self.blog.published
        self.assertEqual((name, post, address, blogger, published), ('sopulin blogi', 'testipostaus', 'url', 'sopuli', '1.1.2022'))

    def test_blog_string(self):
        expected = 'sopuli: sopulin blogi, testipostaus, 1.1.2022, (url)'
        actual = str(self.blog)
        self.assertEqual(actual, expected)
