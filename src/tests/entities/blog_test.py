import unittest

from entities.item import Blog

class TestBlog(unittest.TestCase):
    def setUp(self):
        self.creator = "Tamsin"
        self.blog_name = "Cupful of Kale"
        self.post_title = "Tofu Katsu Curry"
        self.url = "https://cupfulofkale.com/vegan-tofu-katsu-curry/"
        self.published = "1.1.2022"
        self.item_id = "1a2b"
        self.blog = Blog(self.creator, self.blog_name, self.post_title, self.url, self.published, self.item_id)

    def test_init_blog(self):
        self.assertEqual(
            (self.creator, self.blog_name, self.post_title, self.url, self.published),
            ('Tamsin', 'Cupful of Kale', 'Tofu Katsu Curry',
             'https://cupfulofkale.com/vegan-tofu-katsu-curry/', '1.1.2022')
            )

    def test_blog_string(self):
        expected = 'Tamsin: Tofu Katsu Curry (1.1.2022)'
        actual = str(self.blog)
        self.assertEqual(actual, expected)
