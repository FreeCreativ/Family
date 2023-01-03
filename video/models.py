from datetime import datetime

import cv2
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone

from home.models import Comment, Media


# Create your models here.
def thumb(video_file):
    video = cv2.VideoCapture(video_file)
    currentframe = 0
    while True:
        ret, frame = video.read()
        if ret:
            currentframe += 1
            if currentframe % 200 == 0:
                img = cv2.read(frame)
                video.release()
                cv2.destroyAllWindows()
                return img


class Video(Media):
    date = datetime.now()
    datetime_str = "{}-{}-{}/"
    movie_shot = models.ImageField(upload_to='movieShot/' + datetime_str.format(date.year, date.month, date.day),
                                   blank=True)
    video_file = models.FileField(upload_to='video/' + datetime_str.format(date.year, date.month, date.day))
    validators = [FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.name:
            self.name = 'vid-' + str(timezone.now())
            if not self.movie_shot:
                self.movie_shot = thumb(self.video_file)
            super(Video, self).save()
        else:
            super(Video, self).save()

    def thumbnail(self):
        pass


class VideoComment(Comment):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
