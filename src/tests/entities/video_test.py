import unittest

from entities.item import Video

class TestVideo(unittest.TestCase):
    def setUp(self):
        self.video = Video(
            "tglab", "Early mitotic divisions in a Drosophila embryo",
            "https://youtu.be/XSKh-GLQn4E", "3.8.2008"
            )

    def test_init_video(self):
        title = self.video.title
        address = self.video.address
        creator = self.video.creator
        published = self.video.published
        self.assertEqual(
            (title, address, creator, published),
            ("Early mitotic divisions in a Drosophila embryo",
             "https://youtu.be/XSKh-GLQn4E", "tglab", "3.8.2008")
            )

    def test_video_string(self):
        expected = "tglab: Early mitotic divisions in a Drosophila embryo, https://youtu.be/XSKh-GLQn4E, (3.8.2008)"
        actual = str(self.video)
        self.assertEqual(actual, expected)

    def test_video_short_string(self):
        expected = 'tglab: Early mitotic divisions in a Drosophila embryo'
        self.assertEqual(self.video.short_str, expected)
