from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, UpdateView
from account.models import *


# Create your views here.

class RegisterUser(UserCreationForm):
    pass


class Dashboard(LoginRequiredMixin, DetailView):
    template_name = 'account/dashboard.html'
    model = UserAccount
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.model

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data()
        user = UserAccount.objects.get(username=self.request.user)
        context['user_detail'] = user.userdetail
        context['education'] = user.education_set.all()
        context['occupation'] = user.occupation_set.all()
        context['phone_record'] = user.phonerecord_set.all()
        context['emails'] = user.additionalemail_set.all()
        context['diseases'] = user.geneticdisease_set.all()
        return context


class EditProfile(LoginRequiredMixin, UpdateView):
    model = UserAccount
    template_name = 'account/update.html'
