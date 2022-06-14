from django.db import models
from Family.settings import AUTH_USER_MODEL


class Occupation(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    occupation_name = models.TextField(null=False)
    description = models.TextField()
    address = models.TextField(null=False)

    def __str__(self):
        return self.occupation_name
