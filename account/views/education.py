from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from account.forms import EducationForm
from account.models import Education


class EducationListView(LoginRequiredMixin, ListView):
    model = Education
    template_name = 'education/education_list.html'
    context_object_name = 'education_list'
    page_kwarg = 'page'
    ordering = 'school_level'

    def get_queryset(self):
        return Education.objects.filter(user_id=self.request.user)


class EducationDetailView(LoginRequiredMixin, DetailView):
    model = Education
    template_name = 'education/education_detail.html'
    context_object_name = 'education_detail'
    pk_url_kwarg = 'pk'


class EducationCreateView(LoginRequiredMixin, CreateView):
    form_class = EducationForm
    template_name = 'education/education_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(EducationCreateView, self).form_valid(form)


class EducationUpdateView(LoginRequiredMixin, UpdateView):
    model = Education
    template_name = 'education/education_update.html'
    fields = ["name_of_school", "school_level", "year_of_entrance", "year_of_graduation"]
    slug_field = 'id'
    slug_url_kwarg = 'pk'
    success_url = '/'


class EducationDeleteView(LoginRequiredMixin, DeleteView):
    model = Education
    success_url = reverse_lazy('account:education_list')
    slug_field = 'id'
    slug_url_kwarg = 'pk'
    template_name = 'education/education_delete.html'
