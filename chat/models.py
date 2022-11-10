from django.db import models
from Family.settings import AUTH_USER_MODEL

# Create your models here.
from account.models import UserAccount


class Message(models.Model):
    sent_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField
    date_created = models.DateField(auto_created=True, auto_now_add=True)


class ChatMessages(Message):
    pass


class Chat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField
    messages = models.ManyToManyField(Message)
    date_created = models.DateField(auto_created=True, auto_now_add=True)


class Joined(models.Model):
    user = models.ManyToManyField(Chat)


class Group(models.Model):
    group_name = models.CharField(max_length=100, )
    members = models.ManyToManyField(UserAccount, related_name='members')
    admins = models.ManyToManyField(UserAccount, related_name='admins')
    messages = models.ForeignKey(Message, on_delete=models.CASCADE)


class GroupAdmin(models.Model):
    group = models.ManyToManyField(Group, )
