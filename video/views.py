from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from account.views.recent import set_context_data
from video.forms import VideoForm
from video.models import Video


class VideoCreate(LoginRequiredMixin, FormView):
    form_class = VideoForm
    template_name = 'video/video_create.html'
    fields = ['video_file', 'description']
    success_url = reverse_lazy('account:video:video_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(VideoCreate, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.instance.user = self.request.user
        files = request.FILES.getlist('video_file')
        if form.is_valid():
            for f in files:
                vid = Video(video_file=f, user=form.instance.user, description=form.instance.description)
                vid.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class VideoList(LoginRequiredMixin, ListView):
    model = Video
    template_name = 'video/video_list.html'
    context_object_name = 'video_list'
    paginate_by = 20
    page_kwarg = 'page'

    def get_context_data(self, **kwargs):
        context = super(VideoList, self).get_context_data(**kwargs)
        context.update(set_context_data())
        return context


class VideoDetail(LoginRequiredMixin, DetailView):
    model = Video
    template_name = 'video/video_detail.html'
    slug_field = 'name'
    slug_url_kwarg = 'slug'
