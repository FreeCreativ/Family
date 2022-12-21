from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, TemplateView
from django.views.generic.edit import BaseUpdateView
from django_filters.views import FilterView

from account.forms import CreateUserForm, AddUserDetailForm
from account.models import UserAccount
from account.views.recent import set_context_data


class AccountCreateView(CreateView):
    model = UserAccount
    template_name = 'account/register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('account:r_continue')

    def form_valid(self, form):
        form.instance.username = form.instance.first_name + str(form.instance.date_of_birth.year)
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('account:r_continue')


class UserDetailCreateView(LoginRequiredMixin, UpdateView):
    template_name = 'account/register.html'
    form_class = AddUserDetailForm

    def get_object(self, queryset=None):
        return UserAccount.objects.get(username=self.request.user)

    def get_success_url(self):
        return reverse_lazy('account:profile', kwargs={'username': self.object})


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context.update(set_context_data())
        return context


class ProfileView(LoginRequiredMixin, DetailView, BaseUpdateView):
    fields = ['profile_image', ]
    template_name = 'account/profile.html'
    model = UserAccount
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data()
        user = self.object
        context.update(set_context_data())
        context['education'] = user.education_set.all()
        context['occupation'] = user.occupation_set.all()
        context['phone_record'] = user.phonerecord_set.all()
        context['diseases'] = user.geneticdisease_set.all()
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserAccount
    fields = ['email', 'height', 'profile_image']
    template_name = 'account/update.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_success_url(self):
        return reverse_lazy('account:profile', kwargs={'username': self.object})


class BiographyUpdateView(LoginRequiredMixin, UpdateView):
    model = UserAccount
    fields = ['biography', ]
    template_name = 'account/update.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_success_url(self):
        return reverse_lazy('account:profile', kwargs={'username': self.object})


class UserListView(LoginRequiredMixin, FilterView):
    model = UserAccount
    template_name = 'account/member_list.html'
    context_object_name = 'user_list'
    paginate_by = 40
    page_kwarg = 'page'
    filterset_fields = ['date_of_birth', 'gender', 'genotype']

    def get_queryset(self):
        return UserAccount.living.all()

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context.update(set_context_data())
        return context


class Immortalised(LoginRequiredMixin, FilterView):
    model = UserAccount
    template_name = 'account/member_list.html'
    context_object_name = 'user_list'
    paginate_by = 40
    page_kwarg = 'page'
    filterset_fields = ['date_of_birth', 'gender', 'genotype']

    def get_queryset(self):
        return UserAccount.objects.filter(alive=False)

    def get_context_data(self, **kwargs):
        context = super(Immortalised, self).get_context_data(**kwargs)
        context.update(set_context_data())
        return context
