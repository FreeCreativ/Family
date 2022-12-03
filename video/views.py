from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from video.models import Video


class VideoList(LoginRequiredMixin, ListView):
    model = Video
    template_name = 'video/video_list.html'
    context_object_name = 'video_list'
    paginate_by = 20
    page_kwarg = 'page'


class VideoDetail(LoginRequiredMixin, DetailView):
    model = Video
    template_name = 'video/video_detail.html'
