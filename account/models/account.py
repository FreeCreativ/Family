from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import date

from Family.settings import AUTH_USER_MODEL


def get_parent(user):
    u = UserDetail.objects.filter(user_id__username=user)
    return u.first().get_parent()


def get_spouse(user):
    return UserDetail.objects.filter(user_id__username=user).first().get_parent()


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


class UserAccount(AbstractUser):
    middle_name = models.CharField(max_length=20)
    REQUIRED_FIELDS = ["email", "first_name", "middle_name", "last_name"]

    # def get_absolute_url(self):
    #   return reverse('account:dashboard', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "user account"
        verbose_name_plural = "user accounts"


class UnderAge(models.Manager):
    def get_queryset(self):
        return super(UnderAge, self).get_queryset().filter(age_lte=17).filter(alive=True)


class YoungAdult(models.Manager):
    def get_queryset(self):
        return super(YoungAdult, self).get_queryset().filter(alive=True).filter(age_gte=18).filter(age_lte=24)


class Adult(models.Manager):
    def get_queryset(self):
        return super(Adult, self).get_queryset().filter(alive=True).filter(age_gte=25)


class Male(models.Manager):
    def get_queryset(self):
        return super(Male, self).get_queryset().filter(alive=True).filter(gender='male')


class Female(models.Manager):
    def get_queryset(self):
        return super(Female, self).get_queryset().filter(alive=True).filter(gender='female')


class Oldest(models.Manager):
    def get_queryset(self):
        return super(Oldest, self).get_queryset().filter(alive=True).filter(-'age').first()

    def set_oldest(self):
        oldest = OldestAlive(self.get_queryset())
        oldest.save()


class UserDetail(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    alive = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/image', blank=True)
    date_of_birth = models.DateField(verbose_name='Date of birth')
    date_of_death = models.DateField(verbose_name='date of death', null=True, blank=True)
    cause_of_death = models.TextField(null=True, blank=True)
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
    dad = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='father')
    mum = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='mother')

    objects = models.Manager()
    oldest = Oldest()

    def __str__(self):
        return f"{self.user}"

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

    def family_tree(self):
        tree = []
        me = self
        father = get_parent(self.dad)
        grand_father = get_parent(father.dad)
        return tree.append((grand_father, father, me))

    def genealogy(self):
        if self.dad:
            lineage = [self.get_parent()]
            try:
                u = get_parent(self.dad)
            except LookupError:
                lineage = ['You are the oldest know progenitor']
            finally:
                while u is not None:
                    lineage.append(u)
                    u = get_parent(u)
                    return lineage
        else:
            lineage = ['Oldest known progenitor']
            return lineage

    def get_parent(self):
        return self.dad

    def children(self):
        if self.gender == 'male':
            return UserDetail.objects.filter(father=self.id)
        else:
            return UserDetail.objects.filter(mother=self.id)


class OldestAlive(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    rank = models.IntegerField(verbose_name='Rank', primary_key=True, auto_created=True)
    elected = models.DateField(verbose_name='Date Elected', auto_now_add=True)
    retired = models.DateField(verbose_name='Date Retired', blank=True)
    current = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Oldest Alive"
        verbose_name_plural = "Oldest Alive"

    def __str__(self):
        return self.user
