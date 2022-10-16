from django.db import models

from home.models import Comment, Media


# Create your models here.


class Image(Media):
    image_file = models.ImageField(upload_to='photos/')

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.name:
            self.name = 'img-' + str(self.date_of_upload)
            super(Image, self).save()
        else:
            super(Image, self).save()


class ImageComment(Comment):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
