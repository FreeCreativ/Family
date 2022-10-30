from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, CreateView

from account.forms import OccupationForm
from account.models import Occupation


class OccupationCreateView(LoginRequiredMixin, CreateView):
    form_class = OccupationForm
    template_name = 'occupation/occupation_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(OccupationCreateView, self).form_valid(form)


class OccupationUpdateView(LoginRequiredMixin, CreateView):
    form_class = OccupationForm
    template_name = 'occupation/occupation_update.html'
    slug_field = 'id'
    slug_url_kwarg = 'pk'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(OccupationUpdateView, self).form_valid(form)


class OccupationDetailView(LoginRequiredMixin, DetailView):
    model = Occupation
    template_name = 'occupation/occupation_detail.html'
    context_object_name = 'email_detail'
    slug_field = 'id'
    slug_url_kwarg = 'pk'


class OccupationDeleteView(LoginRequiredMixin, DeleteView):
    model = Occupation
    template_name = 'occupation/occupation_delete.html'
    slug_field = 'id'
    slug_url_kwarg = 'pk'
    success_url = reverse_lazy('account:occupation_list')
