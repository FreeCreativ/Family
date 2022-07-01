from django.db import models
from django.urls import reverse

from Family.settings import AUTH_USER_MODEL
from account.id_generator import generate_id


class AdditionalEmail(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, unique=True)
    date_registered = models.DateTimeField(verbose_name='date registered', auto_now_add=True)
    date_modified = models.DateTimeField(verbose_name='date registered', auto_now=True)

    class Meta:
        verbose_name = "Additional Email"
        verbose_name_plural = "Additional Emails"

    def __str__(self):
        return self.email

    def create_id(self):
        return str(self.user) + generate_id(self.date_registered)[:3]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.id = self.create_id()
        super(AdditionalEmail, self).save()

    def get_absolute_url(self):
        return reverse('account:email_detail', kwargs={'pk': self.id})
