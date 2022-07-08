from django.views.generic import ListView, DetailView

from video.models import Video


class PublicVideoListView(ListView):
    model = Video
    template_name = 'public/media_list.html'

    def get_queryset(self):
        super(PublicVideoListView, self).get_queryset().filter(public=True)


class PublicVideoDetailView(DetailView):
    model = Video
    template_name = 'public/media_detail.html'
