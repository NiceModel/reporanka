import unittest

from entities.blog import Blog

class TestBlog(unittest.TestCase):
    def setUp(self):
        self.blog = Blog("sopuli", "testipostaus",  "sopulin blogi", "url", "1.1.2022")

    def test_init_blog(self):
        name = self.blog.name
        post = self.blog.post
        address = self.blog.address
        blogger = self.blog.blogger
        published = self.blog.published
        self.assertEqual((name, post, address, blogger, published), ("testipostaus", "sopulin blogi", "url", "sopuli", "1.1.2022"))

    def test_blog_string(self):
        expected = "sopuli: testipostaus, sopulin blogi, 1.1.2022, (url)"
        actual = str(self.blog)
        self.assertEqual(actual, expected)
