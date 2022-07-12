from django.views.generic import ListView

from image.models import Image


class PublicImageListView(ListView):
    model = Image
    template_name = 'public/media_list.html'

    def get_queryset(self):
        return super(PublicImageListView, self).get_queryset().filter(public=True)


class PublicImageDetailView(ListView):
    model = Image
    template_name = 'public/media_detail.html'

    def get_queryset(self):
        return super(PublicImageDetailView, self).get_queryset().filter(public=True)
