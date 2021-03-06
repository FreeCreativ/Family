from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, ListView

from account.forms import NewUserForm, AddUserDetailForm
from account.models import UserDetail, UserAccount


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

    def get_object(self, queryset=None):
        return UserAccount.objects.get(username=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data()
        user = UserAccount.objects.get(username=self.request.user)
        if UserDetail.objects.filter(user=user).exists():
            context['user_detail'] = user.userdetail
            context['education'] = user.education_set.all()
            context['occupation'] = user.occupation_set.all()
            context['phone_record'] = user.phonerecord_set.all()
            context['emails'] = user.additionalemail_set.all()
            context['diseases'] = user.geneticdisease_set.all()
            return context
        else:
            return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserDetail
    fields = ['height', 'image']
    template_name = 'account/update.html'

    def get_object(self, queryset=None):
        return UserDetail.objects.get(user=self.request.user)


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
