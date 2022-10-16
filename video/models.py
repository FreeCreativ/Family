from django.db import models

from home.models import Comment, Media


# Create your models here.


class Video(Media):
    video_file = models.FileField(upload_to='videoF/')

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.name:
            self.name = 'img-' + str(self.date_of_upload)
            super(Video, self).save()
        else:
            super(Video, self).save()


class VideoComment(Comment):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
