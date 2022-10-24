from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, ListView
from django.views.generic.edit import BaseUpdateView

from account.forms import CreateUserForm, AddUserDetailForm, BiographyForm
from account.models import UserAccount
from account.views.recent import set_context_data


class AccountCreateView(CreateView):
    model = UserAccount
    template_name = 'account/register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('account:r_continue')

    def form_valid(self, form):
        form.instance.username = form.instance.first_name + str(form.instance.date_of_birth.year)
        return super(AccountCreateView, self).form_valid(form)


class UserDetailCreateView(LoginRequiredMixin, UpdateView):
    template_name = 'account/register.html'
    form_class = AddUserDetailForm

    def get_object(self, queryset=None):
        return UserAccount.objects.get(username=self.request.user)


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'account/dashboard.html'
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
        context['emails'] = user.additionalemail_set.all()
        context['diseases'] = user.geneticdisease_set.all()
        return context


class ImageForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['profile_image', ]


class DashboardView(ProfileView, BaseUpdateView):
    fields = ['profile_image', ]

    def get_object(self, queryset=None):
        return UserAccount.objects.get(username=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        # context['image_form'] = ImageForm
        # context['biography_form'] = BiographyForm
        return context

    def form_valid(self, form):
        super(DashboardView, self).form_valid(form)
        return reverse_lazy('account:dashboard', )


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserAccount
    fields = ['height', 'profile_image']
    template_name = 'account/update.html'
    success_url = reverse_lazy('account:dashboard')
    slug_field = 'username'
    slug_url_kwarg = 'username'


class ProfilePictureUpdateView(LoginRequiredMixin, UpdateView):
    model = UserAccount
    fields = ['profile_image', ]
    template_name = 'account/update.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_success_url(self):
        return reverse_lazy('account:dashboard', )


class BiographyUpdateView(LoginRequiredMixin, UpdateView):
    model = UserAccount
    fields = ['biography', ]
    template_name = 'account/update.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_success_url(self):
        return reverse_lazy('account:dashboard', kwargs={'username': self.object})


class UserListView(LoginRequiredMixin, ListView):
    model = UserAccount
    template_name = 'account/member_list.html'
    context_object_name = 'user_list'
    ordering = 'date_of_birth'
    paginate_by = 40
    page_kwarg = 'page'

    extra_context = {
        'page_robots': u'INDEX, NOFOLLOW',
        'page_description': u'Napravi novi nalog',
        'page_keywords': u'registracija, registriranje, novi nalog, napravi nalog',
    }
