import os

import django_filters
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.text import slugify
from django.views.generic import DetailView, FormView, DeleteView
from django_filters import FilterSet
from django_filters.views import FilterView

from Family.settings import BASE_DIR
from account.models import UserAccount
from video.forms import VideoForm
from video.models import Video


class VideoFilter(FilterSet):
    date_of_upload = django_filters.NumberFilter(field_name='date_of_upload', lookup_expr='year')
    month_of_upload = django_filters.NumberFilter(field_name='date_of_upload', lookup_expr='month')
    day_of_upload = django_filters.NumberFilter(field_name='date_of_upload', lookup_expr='day')

    class Meta:
        model = Video
        fields = ['date_of_upload']


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
            if files.__len__() <= 1:
                for video_file in files:
                    name = 'vid-'
                    name += slugify(timezone.now())
                    vid = Video(video_file=video_file, user=form.instance.user, description=form.instance.description,
                                name=name)
                    vid.save()
                return self.form_valid(form)
            elif files.__len__() > 1:
                index = 1
                for video_file in files:
                    name = 'vid-'
                    name += slugify(timezone.now())
                    description = form.instance.description + " " + str(index)
                    vid = Video(video_file=video_file, user=form.instance.user, description=description,
                                name=name)
                    vid.save()
                    index += 1
                return self.form_valid(form)
        else:
            return self.form_invalid(form)


class VideoList(LoginRequiredMixin, FilterView):
    model = Video
    template_name = 'video/video_list.html'
    context_object_name = 'video_list'
    paginate_by = 20
    page_kwarg = 'page'
    filterset_class = VideoFilter


class MyVideoList(LoginRequiredMixin, FilterView):
    model = Video
    template_name = 'video/video_list.html'
    context_object_name = 'video_list'
    paginate_by = 20
    page_kwarg = 'page'
    filterset_class = VideoFilter

    def get_queryset(self):
        return super(MyVideoList, self).get_queryset().filter(user=self.request.user)


class UserVideoList(LoginRequiredMixin, FilterView):
    model = Video
    template_name = 'video/video_list.html'
    context_object_name = 'video_list'
    paginate_by = 20
    page_kwarg = 'page'
    filterset_class = VideoFilter
    slug_field = 'user'
    slug_url_kwarg = 'username'

    def get_queryset(self):
        username = UserAccount.objects.get(username=self.kwargs.get('username')).id
        return super().get_queryset().filter(user=username)


class VideoDetail(LoginRequiredMixin, DetailView):
    model = Video
    template_name = 'video/video_detail.html'
    slug_field = 'name'
    slug_url_kwarg = 'slug'


class VideoDelete(DeleteView):
    model = Video  #

    def form_valid(self, form):
        os.remove(os.path.join(BASE_DIR, 'media', self.object.movie_shot))
        return super().form_valid(form)
