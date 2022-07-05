from django.db import models

from home.models import Comment, Media


# Create your models here.


class Video(Media):
    video_file = models.FileField(upload_to='videoF/')


class VideoComment(Comment):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
