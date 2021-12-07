import unittest

from entities.video import Video

class TestVideo(unittest.TestCase):

    def test_init_video(self):
        self.video = Video("Video", "urli", "sopuli", "1.1.2022")
        title = self.video.title
        address = self.video.address
        creator = self.video.creator
        published = self.video.published
        self.assertEqual((title, address, creator, published), ("Video", "urli", "sopuli", "1.1.2022"))

    def test_video_string(self):
        self.video = Video("Video", "urli", "sopuli", "1.1.2022")
        expected = "Video: sopuli, urli, (1.1.2022)"
        actual = str(self.video)
        self.assertEqual(actual, expected)