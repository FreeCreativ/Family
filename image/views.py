import django_filters
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, FormView
from django_filters import FilterSet
from django_filters.views import FilterView

from account.models import UserAccount
from image.forms import ImageForm
from image.models import Image


class ImageFilter(FilterSet):
    date_of_upload = django_filters.NumberFilter(field_name='date_of_upload', lookup_expr='year')
    month_of_upload = django_filters.NumberFilter(field_name='date_of_upload', lookup_expr='month')
    day_of_upload = django_filters.NumberFilter(field_name='date_of_upload', lookup_expr='day')

    class Meta:
        model = Image
        fields = ['date_of_upload']


class UploadImageView(LoginRequiredMixin, FormView):
    form_class = ImageForm
    template_name = 'image/image_create.html'
    success_url = reverse_lazy('account:image:my_image_list')
    slug_field = 'name'
    slug_url_kwarg = 'slug'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.instance.author = self.request.user
        files = request.FILES.getlist('image_file')
        if form.is_valid():
            for f in files:
                img = Image(image_file=f, user=form.instance.author, description=form.instance.description)
                img.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ImageListView(LoginRequiredMixin, FilterView):
    model = Image
    template_name = 'image/image_list.html'
    paginate_by = 42
    context_object_name = 'image_list'
    ordering = '-date_of_upload'
    page_kwarg = 'page'
    filterset_class = ImageFilter


class MyImageListView(LoginRequiredMixin, FilterView):
    model = Image
    paginate_by = 42
    template_name = 'image/image_list.html'
    context_object_name = 'image_list'
    ordering = 'date_of_upload'
    filterset_class = ImageFilter

    def get_queryset(self):
        return Image.objects.user_media(user=self.request.user)


class UserImageListView(LoginRequiredMixin, FilterView):
    model = Image
    paginate_by = 42
    template_name = 'image/image_list.html'
    context_object_name = 'image_list'
    ordering = 'date_of_upload'
    slug_field = 'user'
    slug_url_kwarg = 'username'
    filterset_class = ImageFilter

    def get_queryset(self):
        username = UserAccount.objects.get(username=self.kwargs.get('username')).id
        return super().get_queryset().filter(user=username)


class MyImageDeleteView(LoginRequiredMixin, DeleteView):
    model = Image
    template_name = 'image/image_delete.html'
    success_url = reverse_lazy('account:my_image_list')

    def form_valid(self, form):
        if self.request.user == self.object.author:
            return super(MyImageDeleteView, self).form_valid(form)
        else:
            return self.form_invalid(form)
