from django.views.generic import ListView, DetailView

from image.models import Image


class ImageListView(ListView):
    model = Image
    template_name = 'image/image_list.html'
    paginate_by = 40
    context_object_name = 'image_list'


class ImageDetailView(DetailView):
    model = Image
