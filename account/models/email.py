from django.db import models
from Family.settings import AUTH_USER_MODEL


class AdditionalEmail(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, unique=True)

    class Meta:
        verbose_name = "Additional Email"
        verbose_name_plural = "Additional Emails"

    def __str__(self):
        return self.email
