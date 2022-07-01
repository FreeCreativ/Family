from django.db import models
from Family.settings import AUTH_USER_MODEL


class Statistics(models.Manager):
    def hereditary(self):
        return self.filter(type='H')

    def acquired(self):
        return self.filter('A')


class GeneticDisease(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    disease_name = models.CharField(max_length=100)
    date_of_infection = models.DateField('date infected')
    type_choices = [('H', 'Hereditary'), ('A', 'Acquired')]
    type = models.CharField(max_length=11, choices=type_choices)

    def __str__(self):
        return self.disease_name
