import unittest

from entities.blog import Blog

class TestBlog(unittest.TestCase):

    def test_init_blog(self):
        self.blog = Blog("SopulinBlogi", "testaus",  "sopuli", "urli", "1.1.2022")
        name = self.blog.name
        post = self.blog.post
        address = self.blog.address
        blogger = self.blog.blogger
        published = self.blog.published
        self.assertEqual((name, post, address, blogger, published), ("SopulinBlogi", "testaus", "urli", "sopuli", "1.1.2022"))

    def test_blog_string(self):
        self.blog = Blog("SopulinBlogi", "testaus",  "sopuli", "urli", "1.1.2022")
        expected = "SopulinBlogi: testaus, urli, sopuli, (1.1.2022)"
        actual = str(self.blog)
        self.assertEqual(actual, expected)

    




