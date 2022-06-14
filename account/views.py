from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, FormView

from account.forms import UserRegisterForm, UserDetailForm
from account.models import *


# Create your views here.

class RegisterUser(FormView):
    template_name = 'account/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('account:r_continue')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()


class RegisterUserDetail(FormView):
    template_name = 'account/register.html'
    form_class = UserDetailForm
    success_url = reverse_lazy('account:dashboard')


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
