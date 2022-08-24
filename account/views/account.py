from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, ListView

from account.forms import NewUserForm, AddUserDetailForm
from account.models import UserAccount
from account.views.recent import set_context_data


class AccountCreateView(CreateView):
    model = UserAccount
    template_name = 'account/register.html'
    form_class = NewUserForm
    success_url = reverse_lazy('account:r_continue')


class UserDetailCreateView(LoginRequiredMixin, CreateView):
    template_name = 'account/register.html'
    form_class = AddUserDetailForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(UserDetailCreateView, self).form_valid(form)


class Dashboard(LoginRequiredMixin, DetailView):
    template_name = 'account/dashboard.html'
    model = UserAccount
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    # def get_object(self, queryset=None):
    #     return UserAccount.objects.get(username=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data()
        user = self.object
        context.update(set_context_data())
        context['education'] = user.education_set.all()
        context['occupation'] = user.occupation_set.all()
        context['phone_record'] = user.phonerecord_set.all()
        context['emails'] = user.additionalemail_set.all()
        context['diseases'] = user.geneticdisease_set.all()
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserAccount
    fields = ['height', 'image']
    template_name = 'account/update.html'
    success_url = reverse_lazy('account:dashboard')

    def get_object(self, queryset=None):
        return UserAccount.objects.get(user=self.request.user)


class ProfilePictureUpdateView(LoginRequiredMixin, UpdateView):
    model = UserAccount
    fields = ['image', ]
    success_url = reverse_lazy('account:dashboard')
    template_name = 'account/update.html'

    def get_object(self, queryset=None):
        return UserAccount.objects.get(user=self.request.user)


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
