from entities.video import Video
from utilities.csv_utilities import read_videos_csv, write_videos_csv

class VideoRepository:

    def __init__(self, path=NULL):
        self._path = path
        self._videos = read_videos_csv(self._path)

    def find_all(self):
        return self._videos

    def create(self, video):
        if isinstance(video, Video):
            if not self._is_duplicate(video):
                self._videos.append(video)
                write_videos_csv(video, self._path)
                return video
            return "duplicate"
        raise TypeError(
            f"Object should be <class 'Video'>, but was {type(video)}")

    def _is_duplicate(self, new_video):
        for video in self._videos:
            if str(video) == str(new_video):
                return True
        return False

VIDEO_REPOSITORY = VideoRepository()