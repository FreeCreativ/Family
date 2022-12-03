from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView
from django_filters.views import FilterView

from image.models import Image


class UploadImageView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['image_file', 'description', ]
    template_name = 'image/image_create.html'
    success_url = reverse_lazy('account:image:my_image_list')
    slug_field = 'name'
    slug_url_kwarg = 'slug'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(UploadImageView, self).form_valid(form)


# class ImageListView(LoginRequiredMixin, ListView):
#     model = Image
#     template_name = 'image/image_list.html'
#     paginate_by = 40
#     context_object_name = 'image_list'
#     ordering = '-date_of_upload'
#     page_kwarg = 'page'
class ImageListView(LoginRequiredMixin, FilterView):
    model = Image
    template_name = 'image/image_list.html'
    paginate_by = 40
    context_object_name = 'image_list'
    ordering = '-date_of_upload'
    page_kwarg = 'page'
    filterset_fields = ['date_of_upload', 'is_public', 'user']


class MyImageListView(LoginRequiredMixin, ListView):
    model = Image
    paginate_by = 40
    template_name = 'image/image_list.html'
    context_object_name = 'image_list'

    def get_queryset(self):
        return Image.objects.my_media(user=self.request.user)


class MyImageDeleteView(LoginRequiredMixin, DeleteView):
    model = Image
    template_name = 'image/image_delete.html'
    success_url = reverse_lazy('account:my_image_list')

    def form_valid(self, form):
        if self.request.user == self.object.user:
            return super(MyImageDeleteView, self).form_valid(form)
        else:
            return self.form_invalid(form)
