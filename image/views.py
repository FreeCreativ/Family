from django.contrib.auth.mixins import LoginRequiredMixin
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
    pass
