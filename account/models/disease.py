from django.db import models
from django.urls import reverse

from Family.settings import AUTH_USER_MODEL
from account.generator import generate_id


class Statistics(models.Manager):
    def hereditary(self):
        return self.filter(type='H')

    def acquired(self):
        return self.filter('A')

    def disease_average_age_of_occurrence(self, disease_name):
        age_sum = 0
        disease_list = self.filter(disease_name=disease_name)
        for disease in disease_list:
            age_sum += disease.age_of_infection
            age_average = age_sum / disease_list.count()
            return age_average


class Disease(models.Model):
    name_of_disease = models.CharField(max_length=50)
    type_of_disease = models.CharField(max_length=50)


class GeneticDisease(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    age_of_infection = models.IntegerField('age of infection')
    disease_name = models.CharField(max_length=100)
    date_of_infection = models.DateField('date infected')
    type_choices = [('H', 'Hereditary'), ('A', 'Acquired')]
    type = models.CharField(max_length=11, choices=type_choices)

    def __str__(self):
        return self.disease_name

    def get_absolute_url(self):
        return reverse('account:', kwargs={'pk': self.id})

    def create_id(self):
        return str(self.user) + self.disease_name + self.type + generate_id(self.age_of_infection)[:3]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.id = self.create_id()
        super(GeneticDisease, self).save()
