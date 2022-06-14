from django.db import models
from Family.settings import AUTH_USER_MODEL


class Education(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    name_of_school = models.TextField(
        verbose_name='Name of school', default='School')
    year_of_entrance = models.DateField(verbose_name='Year of Entrance')
    year_of_graduation = models.DateField(
        verbose_name='Year Graduated', blank=True)
    level_choice = (
        ('E', 'Elementary'),
        ('S', 'Secondary'),
        ('T', 'Tertiary'),
        ('P', 'Post Grad'),
    )
    school_type = models.CharField(max_length=15, choices=level_choice)

    class Meta:
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.name_of_school}, {self.year_of_graduation}"

    def duration(self):
        if self.year_of_graduation:
            return self.year_of_graduation - self.year_of_entrance
        else:
            return 'You are yet to graduate'
