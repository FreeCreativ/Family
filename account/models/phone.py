from django.db import models
from Family.settings import AUTH_USER_MODEL


class PhoneRecord(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(default='+234', max_length=20, unique=True)

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"

    def __str__(self):
        return self.phone_number
