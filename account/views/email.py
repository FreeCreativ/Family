from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, CreateView

from account.forms import EmailForm
from account.models import AdditionalEmail


class EmailListView(LoginRequiredMixin, ListView):
    model = AdditionalEmail
    context_object_name = 'email_list'
    template_name = 'email/email_list.html'
    page_kwarg = 'page'
    ordering = 'date_registered'


class EmailCreateView(LoginRequiredMixin, CreateView):
    form_class = EmailForm
    template_name = 'email/email_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(EmailCreateView, self).form_valid(form)


class EmailDetailView(LoginRequiredMixin, DetailView):
    model = AdditionalEmail
    template_name = 'email/email_detail.html'
    context_object_name = 'email_detail'
    slug_field = 'id'
    slug_url_kwarg = 'pk'


class EmailDeleteView(LoginRequiredMixin, DeleteView):
    model = AdditionalEmail
    template_name = 'email/email_delete.html'
    slug_field = 'id'
    slug_url_kwarg = 'pk'
    success_url = reverse_lazy('account:email_list')
