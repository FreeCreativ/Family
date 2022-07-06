from django.db import models

# Create your models here.
from django.utils.text import slugify

from Family.settings import AUTH_USER_MODEL
from home.models import Comment


class Post(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=300)
    slug = models.SlugField(headline, max_length=300, primary_key=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.slug:
            self.slug = slugify(self.headline)
            super(Post, self).save()
        else:
            super(Post, self).save()


class PostComment(Comment):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
