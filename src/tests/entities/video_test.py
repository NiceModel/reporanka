import unittest

from entities.item import Video

class TestVideo(unittest.TestCase):
    def setUp(self):
        self.creator = "tglab"
        self.title = "Early mitotic divisions in a Drosophila embryo"
        self.url = "https://youtu.be/XSKh-GLQn4E"
        self.published = "3.8.2008"
        self.item_id = "5e6f"
        self.video = Video(self.creator, self.title, self.url, self.published, self.item_id)

    def test_init_video(self):
        self.assertEqual(
            (self.creator, self.title, self.url, self.published),
            ('tglab', 'Early mitotic divisions in a Drosophila embryo', 'https://youtu.be/XSKh-GLQn4E', '3.8.2008')
        )

    def test_video_string(self):
        expected = "tglab: Early mitotic divisions in a Drosophila embryo (3.8.2008)"
        actual = str(self.video)
        self.assertEqual(actual, expected)
