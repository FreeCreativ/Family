from datetime import datetime

from django.db import models
from django.utils import timezone

from home.models import Comment, Media


# Create your models here.


class Image(Media):
    date = datetime.now()
    datetime_str = "{}-{}-{}/"
    image_file = models.ImageField(upload_to='images/' + datetime_str.format(date.year, date.month, date.day))

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.name:
            self.name = 'img-' + str(timezone.now())
            super(Image, self).save()
        else:
            super(Image, self).save()
