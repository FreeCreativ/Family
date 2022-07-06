from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView

from account.forms import GeneticDiseaseForm
from account.models import GeneticDisease


class DiseaseListView(LoginRequiredMixin, ListView):
    model = GeneticDisease
    context_object_name = 'disease_list'
    template_name = 'disease/disease_list.html'
    page_kwarg = 'page'
    ordering = 'date_registered'


class DiseaseCreateView(LoginRequiredMixin, CreateView):
    form_class = GeneticDiseaseForm
    template_name = 'disease/disease_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(DiseaseCreateView, self).form_valid(form)


class DiseaseDetailView(LoginRequiredMixin, DetailView):
    model = GeneticDisease
    template_name = 'disease/disease_detail.html'
    context_object_name = 'disease_detail'
    slug_field = 'id'
    slug_url_kwarg = 'pk'


class DiseaseDeleteView(LoginRequiredMixin, DeleteView):
    model = GeneticDisease
    template_name = 'disease/disease_delete.html'


class DiseaseUpdateView(LoginRequiredMixin, UpdateView):
    form_class = GeneticDiseaseForm
    template_name = 'occupation/occupation_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(DiseaseUpdateView, self).form_valid(form)
