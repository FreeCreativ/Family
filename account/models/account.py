import datetime

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.datetime_safe import date

from Family.settings import AUTH_USER_MODEL
from account.generator import duration


def get_parent(user):
    u = UserAccount.objects.get(username=user)
    return u.get_father()


def get_spouse(user):
    return UserAccount.objects.filter(user_id__username=user).first().get_father()


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


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


# class Oldest(models.Manager):
#     def get_queryset(self):
#         old_list = super(Oldest, self).get_queryset().filter(alive=True).order_by('date_of_birth')[:10]
#         new_old_list = super(Oldest, self).get_queryset().filter(alive=True).order_by('date_of_birth')[1:10]
#
#         for person in new_old_list:
#             if person.date_of_birth == old_list.first().date_of_birth:
#                 return old_list.order_by('date_registered').first()
#
#     def get_oldest(self):
#         current_oldest = OldestAlive.objects.get_current_oldest()
#         if current_oldest.user_id != self.get_queryset().user:
#             new_oldest = OldestAlive()
#             new_oldest.user = self.get_queryset().user
#             new_oldest.save()
#             return OldestAlive.objects.get_current_oldest()
#         else:
#             return current_oldest

def gen_height():
    h = 30
    heights = [
        ('30', '30'),
    ]

    while h <= 244:
        h += 1
        heights.append((h, h))
    return tuple(heights)


class UserAccount(AbstractUser):
    middle_name = models.CharField(max_length=20)
    alive = models.BooleanField(default=True)
    profile_image = models.ImageField(upload_to='img', blank=True)
    date_of_birth = models.DateField(verbose_name='Date of birth', blank=True, null=True)
    date_of_death = models.DateField(verbose_name='date of death', null=True, blank=True)
    date_modified = models.DateTimeField(verbose_name='date registered', auto_now=True)
    biography = models.TextField(blank=True)
    cause_of_death = models.TextField(blank=True)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(max_length=7, choices=gender_choices, blank=True)
    heights = gen_height()
    height = models.IntegerField(verbose_name='height (cm)', blank=True, null=True, choices=heights)
    blood_group_choices = [('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')]
    blood_group = models.CharField(max_length=3, blank=True, choices=blood_group_choices)
    geno_type_choices = [('AA', 'AA'), ('AS', 'AS'), ('SS', 'SS')]
    genotype = models.CharField(max_length=3, blank=True, choices=geno_type_choices)
    dad = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='father')
    mum = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='mother')
    objects = UserManager()
    living = Alive()
    REQUIRED_FIELDS = ["email", "date_of_birth", "first_name", "middle_name", "last_name"]

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse_lazy('account:profile', kwargs={'username': self.username})

    def children(self):
        if self.gender == 'M':
            return UserAccount.objects.filter(dad=self.id)
        else:
            return UserAccount.objects.filter(mum=self.id)

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
            lineage = ['You are the oldest known progenitor', ]
            return lineage

    class Meta:
        verbose_name = "user account"
        verbose_name_plural = "user accounts"


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
