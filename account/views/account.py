from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, TemplateView
from django.views.generic.edit import BaseUpdateView
import django_filters
from django_filters import FilterSet
from django_filters.views import FilterView

from account.forms import CreateUserForm, AddUserDetailForm
from account.models import UserAccount
from blog.models import Post
from image.models import Image
from video.models import Video


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


def set_context_data():
    latest_posts = Post.objects.order_by('-date_created')[:5]
    latest_images = Image.objects.order_by('-date_of_upload')[:12]
    latest_videos = Video.objects.order_by('-date_of_upload')[:12]
    context = {'latest_posts': latest_posts, 'latest_images': latest_images, 'latest_videos': latest_videos}
    return context


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
        context['education'] = user.education_set.all()
        context['occupation'] = user.occupation_set.all()
        context['phone_record'] = user.phonerecord_set.all()
        context['diseases'] = user.geneticdisease_set.all()
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserAccount
    fields = ['email', 'height', 'profile_image', 'biography']
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


class MemberFilterSet(FilterSet):
    date_of_birth = django_filters.NumberFilter(field_name='date_of_birth', lookup_expr='year')
    month_of_birth = django_filters.NumberFilter(field_name='date_of_birth', lookup_expr='month')
    day_of_birth = django_filters.NumberFilter(field_name='date_of_birth', lookup_expr='day')
    last_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = UserAccount
        fields = ['date_of_birth', 'last_name', 'gender', 'genotype']


class UserListView(LoginRequiredMixin, FilterView):
    model = UserAccount
    template_name = 'account/member_list.html'
    context_object_name = 'user_list'
    paginate_by = 40
    page_kwarg = 'page'
    filterset_class = MemberFilterSet

    def get_queryset(self):
        return UserAccount.living.all()


class Immortalised(LoginRequiredMixin, FilterView):
    model = UserAccount
    template_name = 'account/member_list.html'
    context_object_name = 'user_list'
    paginate_by = 40
    page_kwarg = 'page'
    filterset_fields = ['date_of_birth', 'gender', 'genotype']

    def get_queryset(self):
        return UserAccount.objects.filter(alive=False)
