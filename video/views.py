from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from video.models import Video


class VideoCreate(LoginRequiredMixin, CreateView):
    model = Video
    template_name = 'video/video_create.html'
    fields = ['video_file', 'description']
    success_url = reverse_lazy('account:video:video_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(VideoCreate, self).form_valid(form)


class VideoList(LoginRequiredMixin, ListView):
    model = Video
    template_name = 'video/video_list.html'
    context_object_name = 'video_list'
    paginate_by = 20
    page_kwarg = 'page'


class VideoDetail(LoginRequiredMixin, DetailView):
    model = Video
    template_name = 'video/video_detail.html'
    slug_field = 'name'
    slug_url_kwarg = 'slug'
