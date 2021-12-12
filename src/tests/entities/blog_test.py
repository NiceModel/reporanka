import unittest

from entities.item import Blog

class TestBlog(unittest.TestCase):
    def setUp(self):
        self.blog = Blog(
            "Tamsin", "Cupful of Kale", "Tofu Katsu Curry",
            "https://cupfulofkale.com/vegan-tofu-katsu-curry/", "1.1.2022"
            )

    def test_init_blog(self):
        name = self.blog.name
        post = self.blog.title
        address = self.blog.address
        blogger = self.blog.blogger
        published = self.blog.published
        self.assertEqual(
            (name, post, address, blogger, published),
            ('Cupful of Kale', 'Tofu Katsu Curry',
             'https://cupfulofkale.com/vegan-tofu-katsu-curry/', 'Tamsin', '1.1.2022')
            )

    def test_blog_string(self):
        expected = 'Tamsin: Cupful of Kale, Tofu Katsu Curry, 1.1.2022, (https://cupfulofkale.com/vegan-tofu-katsu-curry/)'
        actual = str(self.blog)
        self.assertEqual(actual, expected)

    def test_blog_short_string(self):
        expected = 'Cupful of Kale: Tofu Katsu Curry'
        self.assertEqual(self.blog.short_str, expected)
