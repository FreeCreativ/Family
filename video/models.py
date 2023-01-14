from datetime import datetime

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone

from home.models import Comment, Media


# Create your models here.
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
            super(Video, self).save()
        else:
            super(Video, self).save()


class VideoComment(Comment):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
