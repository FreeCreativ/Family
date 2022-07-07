import datetime

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.datetime_safe import date

from Family.settings import AUTH_USER_MODEL
from account.generator import duration


def get_parent(user):
    # u = UserDetail.objects.filter(user_id__username=user)
    #
    # parent = UserDetail.objects.filter(user_id__username=user)
    # if u.first().get_father().exists():
    #     return u.first().get_father()
    # else:
    #     return None
    u = UserDetail.objects.get(user=user)
    return u.get_father()


def get_spouse(user):
    return UserDetail.objects.filter(user_id__username=user).first().get_father()


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


class UserAccount(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(max_length=150, unique=True, primary_key=True,
                                help_text=(
                                    "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
                                ),
                                validators=[username_validator],
                                error_messages={
                                    "unique": "A user with that user already exists.",
                                },
                                )
    middle_name = models.CharField(max_length=20)
    REQUIRED_FIELDS = ["email", "first_name", "middle_name", "last_name"]

    class Meta:
        verbose_name = "user account"
        verbose_name_plural = "user accounts"


class Alive(models.Manager):
    def get_queryset(self):
        return super(Alive, self).get_queryset().filter(alive=True)

    def get_user(self, user=None):
        if user != "" or None:
            return self.get(user=user)

    def under_age(self):
        return self.filter(date_of_birth__gte=timezone.now() - datetime.timedelta(days=6574.5))

    def young_adult(self):
        return self.filter(date_of_birth__lt=timezone.now() - datetime.timedelta(days=6574.5)).filter(
            date_of_birth__gte=timezone.now() - datetime.timedelta(days=9131.25))

    def adult(self):
        return self.filter(date_of_birth__lt=timezone.now() - datetime.timedelta(days=9131.25))

    def male(self):
        return self.filter(gender='male')

    def female(self):
        return self.filter(gender='female')

    def count(self):
        return self.count()


class Oldest(models.Manager):
    def get_queryset(self):
        old_list = super(Oldest, self).get_queryset().filter(alive=True).order_by('date_of_birth')[:10]
        new_old_list = super(Oldest, self).get_queryset().filter(alive=True).order_by('date_of_birth')[1:10]

        for person in new_old_list:
            if person.date_of_birth == old_list.first().date_of_birth:
                return old_list.order_by('date_registered').first()

    def get_oldest(self):
        current_oldest = OldestAlive.objects.get_current_oldest()
        if current_oldest.user_id != self.get_queryset().user:
            new_oldest = OldestAlive()
            new_oldest.user = self.get_queryset().user
            new_oldest.save()
            return OldestAlive.objects.get_current_oldest()
        else:
            return current_oldest


class UserDetail(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    alive = models.BooleanField(default=True)
    image = models.ImageField(upload_to='public/image', blank=True)
    date_of_birth = models.DateField(verbose_name='Date of birth')
    date_of_death = models.DateField(verbose_name='date of death', null=True, blank=True)
    date_registered = models.DateTimeField(verbose_name='date registered', auto_now_add=True)
    date_modified = models.DateTimeField(verbose_name='date registered', auto_now=True)
    cause_of_death = models.TextField(null=True, blank=True)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(default='Male', max_length=7, choices=gender_choices)
    heights = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    height = models.CharField(default='M', max_length=10, blank=True, choices=heights)
    blood_group_choices = [('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')]
    blood_group = models.CharField(default='A', max_length=4, blank=True, choices=blood_group_choices)
    geno_type_choices = [('AA', 'AA'), ('AS', 'AS'), ('SS', 'SS')]
    genotype = models.CharField(default='AA', max_length=4, blank=True, choices=geno_type_choices)
    dad = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='father')
    mum = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='mother')
    objects = models.Manager()
    oldest = Oldest()
    living = Alive()

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse('account:dashboard', )

    def children(self):
        if self.gender == 'male':
            return UserDetail.objects.filter(father=self.id)
        else:
            return UserDetail.objects.filter(mother=self.id)

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

    def get_father(self):
        return self.dad

    def get_mother(self):
        return self.mum

    def family_tree(self):
        tree = []
        me = self
        father = get_parent(self.dad)
        grand_father = get_parent(father.dad)
        return tree.append((grand_father, father, me))

    def genealogy(self):
        if self.dad:
            lineage = [self, self.get_father()]
            parent = get_parent(self.dad)
            while parent is not None:
                lineage.append(parent)
                parent = get_parent(parent)
            else:
                lineage.append('Oldest known progenitor', )
                return lineage
        else:
            lineage = ['You are the oldest know progenitor']
            return lineage


class OldestManager(models.Manager):
    def get_current_oldest(self):
        return self.order_by('date_elected').first()


class OldestAlive(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    rank = models.IntegerField(verbose_name='Rank', primary_key=True, auto_created=True)
    date_elected = models.DateField(verbose_name='Date Elected', auto_now_add=True)
    date_retired = models.DateField(verbose_name='Date Retired', blank=True)
    objects = OldestManager()

    class Meta:
        verbose_name = "Oldest Alive"
        verbose_name_plural = "Oldest Alive"

    def __str__(self):
        return self.user

    def duration(self):
        if self.date_retired:
            return duration(self.date_retired, self.date_elected)
        else:
            return 'You are the current oldest person, in the family.'
