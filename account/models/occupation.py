from datetime import datetime

from django.db import models
from django.urls import reverse

from Family.settings import AUTH_USER_MODEL
from account.generator import generate_id


def remove(string):
    ns = ""
    for i in string:
        if not i.isspace() and i != ":" and i != ".":
            ns += i
    return ns


class Occupation(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    occupation_name = models.TextField(null=False)
    description = models.TextField()
    address = models.TextField(null=False)
    date_registered = models.DateTimeField(verbose_name='date registered', auto_now_add=True)
    date_modified = models.DateTimeField(verbose_name='date registered', auto_now=True)

    def __str__(self):
        return self.occupation_name

    def create_id(self):
        return str(self.user) + generate_id(remove(str(datetime.now())))

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.id = self.create_id()
            super(Occupation, self).save()
        else:
            super(Occupation, self).save()

    def get_absolute_url(self):
        return reverse('account:occupation_detail', kwargs={'pk': self.id, 'username': self.user})
