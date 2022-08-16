import django_filters

from account.models import UserAccount


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = UserAccount
        fields = ('date_of_birth', 'date_of_death',)
