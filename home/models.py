from django.db import models
from django.utils import timezone

# Create your models here.
from Family.settings import AUTH_USER_MODEL


class Log(models.Model):
    username = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}, {self.login_time}, {self.logout_time}"

    def session(self):
        sess = self.logout_time - self.login_time
        return sess


class Comment(models.Model):
    created_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['date_created']

    def __str__(self):
        return self.comment


class Media(models.Model):
    created_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_upload = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300, default=timezone.now())
    description = models.TextField()

    class Meta:
        abstract = True
        ordering = ['date_of_upload']
