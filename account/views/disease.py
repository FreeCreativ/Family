from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, DetailView, CreateView, UpdateView

from account.forms import GeneticDiseaseForm
from account.models import GeneticDisease


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
    success_url = '../../'


class DiseaseUpdateView(LoginRequiredMixin, UpdateView):
    form_class = GeneticDiseaseForm
    template_name = 'occupation/occupation_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(DiseaseUpdateView, self).form_valid(form)
