import unittest

from entities.video import Video

class TestVideo(unittest.TestCase):
    def setUp(self):
        self.video = Video("sopuli", "video", "url", "1.1.2022")

    def test_init_video(self):
        title = self.video.title
        address = self.video.address
        creator = self.video.creator
        published = self.video.published
        self.assertEqual((title, address, creator, published), ("video", "url", "sopuli", "1.1.2022"))

    def test_video_string(self):
        expected = "sopuli: video, url, (1.1.2022)"
        actual = str(self.video)
        self.assertEqual(actual, expected)
