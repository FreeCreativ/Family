from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DeleteView

from image.models import Image


class ImageListView(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'image/image_list.html'
    paginate_by = 40
    context_object_name = 'image_list'


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
