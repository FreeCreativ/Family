from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, FormView
from django_filters.views import FilterView

from video.forms import VideoForm
from video.models import Video


class VideoCreate(LoginRequiredMixin, FormView):
    form_class = VideoForm
    template_name = 'video/video_create.html'
    fields = ['video_file', 'description']
    success_url = reverse_lazy('account:video:video_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VideoCreate, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.instance.user = self.request.user
        files = request.FILES.getlist('video_file')
        if form.is_valid():
            for video_file in files:
                name = 'vid-'
                name += slugify(timezone.now())
                vid = Video(video_file=video_file, user=form.instance.user, description=form.instance.description,
                            name=name)
                vid.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class VideoList(LoginRequiredMixin, FilterView):
    model = Video
    template_name = 'video/video_list.html'
    context_object_name = 'video_list'
    paginate_by = 20
    page_kwarg = 'page'
    filterset_fields = ['date_of_upload', 'is_public', ]


class MyVideoList(LoginRequiredMixin, ListView):
    model = Video
    template_name = 'video/video_list.html'
    context_object_name = 'video_list'
    paginate_by = 20
    page_kwarg = 'page'

    def get_queryset(self):
        return super(MyVideoList, self).get_queryset().filter(user=self.request.user)


class VideoDetail(LoginRequiredMixin, DetailView):
    model = Video
    template_name = 'video/video_detail.html'
    slug_field = 'name'
    slug_url_kwarg = 'slug'
