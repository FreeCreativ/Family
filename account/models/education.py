from datetime import timezone

from django.db import models
from django.urls import reverse

from Family.settings import AUTH_USER_MODEL
from account.generator import generate_id, duration


class Education(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    name_of_school = models.TextField(
        verbose_name='Name of school', default='School')
    year_of_entrance = models.DateField(verbose_name='Year of Entrance')
    year_of_graduation = models.DateField(
        verbose_name='Year Graduated', blank=True)
    level_choice = (
        ('Elementary', 'Elementary'),
        ('Secondary', 'Secondary'),
        ('Tertiary', 'Tertiary'),
        ('Post_Graduation', 'Post Graduation'),
    )
    school_level = models.CharField(max_length=15, choices=level_choice)

    def create_id(self):
        return str(self.user) + self.school_level + generate_id(self.year_of_entrance)[:3]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.id = self.create_id()
        super(Education, self).save()

    def get_absolute_url(self):
        return reverse('account:education_detail', kwargs={'username': self.user, 'pk': self.id})

    class Meta:
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.name_of_school}, {self.year_of_graduation}, {self.school_level}"

    def duration(self):
        if self.year_of_graduation:
            return duration(self.year_of_graduation, self.year_of_entrance)
        else:
            return 'You are yet to graduate'
