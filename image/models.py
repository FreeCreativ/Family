from django.db import models

from home.models import Comment, Media


# Create your models here.


class Image(Media):
    image_file = models.ImageField(upload_to='imagef/')


class ImageComment(Comment):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
