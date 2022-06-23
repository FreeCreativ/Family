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


class RegisterEducationView(LoginRequiredMixin, CreateView):
    form_class = EducationForm
    template_name = 'education/register_education_detail.html'

    # def form_valid(self, form):
    #     education = form.save(commit=False)
    #     education.user = self.request.user
    #     education.save()
    #     return super(RegisterEducationView, self).form_valid(form)

    def form_valid(self, form):
        # form.cleaned_data['user'] = self.request.user
        education = form.save(commit=False)
        education.user = self.request.user
        super(RegisterEducationView, self).form_valid(education)


class UpdateEducationView(LoginRequiredMixin, UpdateView):
    model = Education
    template_name = 'education/education_update.html'
    fields = ["name_of_school", "year_of_entrance", "year_of_graduation", "school_level"]
    success_url = '/'


class DeleteEducationView(LoginRequiredMixin, DeleteView):
    model = Education
    success_url = reverse_lazy('account:education_delete')
