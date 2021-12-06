from entities.video import Video
from repositories.video_repository import (VIDEO_REPOSITORY as default_video_repository)
from services.id_generator import (id_generator as default_id_generator)

class VideoService:

    def __init__(self, video_repository = default_video_repository, id_generator = default_id_generator):
        self._video_repository = video_repository
        self._id_generator = id_generator


    def create_video(self, title, address, creator, published):
        video_id = self._id_generator.new_id()
        video = self._video_repository.create(Video(video_id, title, address, creator, published))
        return video

    def find_all_videos(self):
        videos = self._video_repository.find_all()
        return sorted(videos, key=lambda video: video.title.lower())

VIDEO_SERVICE = VideoService()