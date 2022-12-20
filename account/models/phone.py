from django.db import models
from Family.settings import AUTH_USER_MODEL


def gen_country_codes():
    code = 1
    c = '+'
    codes = [
        ('+1', '+1'),
    ]
    while code <= 300:
        code += 1
        c += str(code)
        codes.append((c, c))
        c = '+'
    return tuple(codes)


class PhoneRecord(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    country_codes = models.CharField(max_length=20, choices=gen_country_codes())
    phone_number = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"

    def __str__(self):
        return self.country_codes + self.phone_number
