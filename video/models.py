import os
from datetime import datetime

import cv2
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone

from Family.settings import BASE_DIR
from home.models import Comment, Media


# Create your models here.
class Video(Media):
    date = datetime.now()
    datetime_str = "{}-{}-{}/"
    movie_shot = models.ImageField(upload_to='videoShots/' + datetime_str.format(date.year, date.month, date.day),
                                   blank=True)
    video_file = models.FileField(upload_to='videos/' + datetime_str.format(date.year, date.month, date.day),
                                  max_length=250)
    validators = [FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.name:
            self.name = 'vid-' + str(timezone.now())
            super(Video, self).save()
        else:
            super(Video, self).save()

    def movie_photo(self):
        if self.movie_shot:
            return self.movie_shot
        else:
            location = os.path.join(BASE_DIR, 'media', self.video_file.name)
            video = cv2.VideoCapture(location)
            currentframe = 0
            while True:
                success, frame = video.read()
                if success:
                    currentframe += 10000
                    if currentframe % 10000 == 0:
                        date = datetime.now()
                        datetime_str = "{}-{}-{}/"
                        video_shot_directory = os.path.join(BASE_DIR, 'media/videoShots',
                                                            datetime_str.format(date.year, date.month, date.day))
                        print(video_shot_directory)
                        if not os.path.exists(video_shot_directory):
                            os.makedirs(video_shot_directory)
                        video_shot_location = os.path.join(video_shot_directory, self.name)
                        cv2.imwrite(video_shot_location + '.jpg', frame)
                        self.movie_shot = 'videoShots/' + datetime_str.format(date.year, date.month,
                                                                              date.day) + '/' + self.name + '.jpg'
                        self.save()
                        video.release()
                        cv2.destroyAllWindows()
                    return self.movie_shot


class VideoComment(Comment):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
