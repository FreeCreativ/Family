from django.db import models
from Family.settings import AUTH_USER_MODEL


# Create your models here.
class Chat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField
    date_created = models.DateField(auto_created=True, auto_now_add=True)


class Joined(models.Model):
    user = models.ManyToManyField(Chat)


class Message(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    body = models.TextField
    date_created = models.DateField(auto_created=True, auto_now_add=True)
    
