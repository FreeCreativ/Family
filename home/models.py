from django.db import models

# Create your models here.
from Family.settings import AUTH_USER_MODEL


class Log(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}, {self.login_time}, {self.logout_time}"

    def session(self):
        sess = self.logout_time - self.login_time
        return sess


class Comment(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['date_created']

    def __str__(self):
        return self.comment


class MediaManager(models.Manager):
    def get_queryset(self):
        return super(MediaManager, self).get_queryset().filter(is_public=True)


class MyMedia(models.Manager):

    def my_media(self, user):
        return self.filter(user=user)


class Media(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_upload = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300, primary_key=True)
    description = models.TextField()
    is_public = models.BooleanField(default=True, choices=[("True", "True"), ("False", "False")])
    public = MediaManager()
    objects = MyMedia()

    class Meta:
        abstract = True
        ordering = ['date_of_upload']
