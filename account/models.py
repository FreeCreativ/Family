from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.datetime_safe import date


# from Family.settings import UserAccount


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        manager = super(CustomUserManager, self)._create_user()

    def oldest_alive(self):
        return self.annotate(
            num_responses=models.Count("response")
        )


class UserAccount(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    middle_name = models.CharField(max_length=20)
    REQUIRED_FIELDS = ["email", "first_name", "middle_name", "last_name"]


class UserDetail(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    date_of_birth = models.DateField(verbose_name='Date of birth')
    date_of_death = models.DateField(verbose_name='date of death', null=True, blank=True)
    cause_of_death = models.TextField(null=True)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(default='Male', max_length=7, choices=gender_choices)
    heights = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    height = models.CharField(default='5 feet', max_length=10, blank=True, choices=heights)
    blood_group_choices = [('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')]
    blood_group = models.CharField(default='A', max_length=4, blank=True, choices=blood_group_choices)
    geno_type_choices = [('AA', 'AA'), ('AS', 'AS'), ('SS', 'SS')]
    genotype = models.CharField(default='AA', max_length=4, blank=True, choices=geno_type_choices)
    image = models.ImageField(upload_to='media/image', blank=True)
    alive = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse("account:dashboard", kwargs={"username": self.user})

    def died(self):
        if self.date_of_death:
            length = calculate_age(self.date_of_death)
            if length == 0:
                days_in_year = 365.2425

                length = (date.today() - self.date_of_birth).days % days_in_year
                length = length * 30
                return f"Died {length} months ago"
            else:
                return f"Died {length} years ago"
        else:
            return 'This person has been recorded dead, but date of death is unavailable'

    def age(self):
        if self.alive:
            age = calculate_age(self.date_of_birth)
            if age == 0:
                # days_in_year = 365.2425
                age_in_days = (date.today() - self.date_of_birth).days
                if age_in_days < 30:
                    return f"{age_in_days} days old"
                else:
                    age_in_months = age_in_days / 30
                    if age_in_months == 1:
                        return f"{age_in_months} month old"
                    else:
                        return f"{age_in_months} months old"
            elif age == 1:
                return f"{age} Year old"
            else:
                return f"{age} Years old"
        else:
            return str(self.died())

    # def __str__(self):
    #     return f"{self.surname}, {self.fN}, {self.middleName}"
    #     return '%s %s %s' % (self.last_name, self.first_name, self.middle_name)

    # def lineage(self, user_id=None):
    #     line = {}
    #     if user_id:
    #         u = UserDetail.objects.get(user=user_id)
    #         parent = u.parent
    #         if parent:
    #             line[u.id] = u
    #             self.lineage(parent)
    #         else:
    #             return line
    #     else:
    #         u = UserDetail.objects.get(user=self.user)
    #         parent = u.parent
    #         if parent:
    #             line[u.id] = u
    #             self.lineage(parent)
    #         else:
    #             return line
    def get_parent(self):
        return self.parent

    def lineage(self):
        pass
    


class Education(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    name_of_school = models.TextField(verbose_name='Name of school', default='School')
    year_of_entrance = models.DateField(verbose_name='Year of Entrance')
    year_of_graduation = models.DateField(verbose_name='Year Graduated', blank=True)
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
        # return self.name_of_school, self.year_of_graduation
        return f"{self.name_of_school}, {self.year_of_graduation}"

    def duration(self):
        if self.year_of_graduation:
            return self.year_of_graduation - self.year_of_entrance
        else:
            return 'You are yet to graduate'


class SpouseOf(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    spouse_id = models.CharField(null=True, blank=True, max_length=20)
    when = models.DateField('wedding date')
    maiden_name = models.CharField(max_length=30, unique=False)

    def __str__(self):
        return f"The spouse of {self.user} is {self.spouse_id}"


class Occupation(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    occupation_name = models.TextField(null=False)
    description = models.TextField()
    address = models.TextField(null=False)

    def __str__(self):
        return self.occupation_name


class PhoneRecord(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    phone_number = models.CharField(default='+234', max_length=20, unique=True)

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"

    def __str__(self):
        return self.phone_number


class AdditionalEmail(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, unique=True)

    class Meta:
        verbose_name = "Additional Email"
        verbose_name_plural = "Additional Emails"

    def __str__(self):
        return self.email


class OldestAlive(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    rank = models.IntegerField(verbose_name='Rank', primary_key=True, auto_created=True)
    elected = models.DateField(verbose_name='Date Elected')
    retired = models.DateField(verbose_name='Date Retired', blank=True)
    current = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Oldest Alive"
        verbose_name_plural = "Oldest Alive"

    def __str__(self):
        return self.user


class GeneticDisease(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    disease_name = models.CharField(max_length=100)
    date_of_infection = models.DateField('date infected')
    type_choices = [('H', 'Hereditary'), ('C', 'Contacted')]
    type = models.CharField(max_length=11, choices=type_choices)

    def __str__(self):
        return self.disease_name