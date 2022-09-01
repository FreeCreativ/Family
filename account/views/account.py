from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, ListView

from account.forms import UpdateUserForm, AddUserDetailForm
from account.models import UserAccount
from account.views.recent import set_context_data


class AccountCreateView(CreateView):
    model = UserAccount
    template_name = 'account/register.html'
    form_class = UpdateUserForm
    success_url = reverse_lazy('account:r_continue')


class UserDetailCreateView(LoginRequiredMixin, UpdateView):
    template_name = 'account/register.html'
    form_class = AddUserDetailForm

    def get_object(self, queryset=None):
        return UserAccount.objects.get(username=self.request.user)


class Profile(LoginRequiredMixin, DetailView):
    template_name = 'account/dashboard.html'
    model = UserAccount
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data()
        user = self.object
        context.update(set_context_data())
        context['education'] = user.education_set.all()
        context['occupation'] = user.occupation_set.all()
        context['phone_record'] = user.phonerecord_set.all()
        context['emails'] = user.additionalemail_set.all()
        context['diseases'] = user.geneticdisease_set.all()
        return context


class ImageForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['profile_image']


class Dashboard(Profile):
    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['imageform'] = ImageForm
        return context

    def get_object(self, queryset=None):
        return UserAccount.objects.get(username=self.request.user)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserAccount
    fields = ['height', 'profile_image']
    template_name = 'account/update.html'
    success_url = reverse_lazy('account:dashboard')

    def get_object(self, queryset=None):
        return UserAccount.objects.get(username=self.request.user)


class ProfilePictureUpdateView(LoginRequiredMixin, UpdateView):
    model = UserAccount
    fields = ['profile_image', ]
    success_url = reverse_lazy('account:dashboard')
    template_name = 'account/update.html'

    def get_object(self, queryset=None):
        return UserAccount.objects.get(username=self.request.user)


class UserListView(LoginRequiredMixin, ListView):
    model = UserAccount
    template_name = 'account/member_list.html'
    context_object_name = 'user_list'
    paginate_by = 40
    page_kwarg = 'page'

    extra_context = {
        'page_robots': u'INDEX, NOFOLLOW',
        'page_description': u'Napravi novi nalog',
        'page_keywords': u'registracija, registriranje, novi nalog, napravi nalog',
    }
