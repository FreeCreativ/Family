from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, FormView
from django_filters.views import FilterView

from account.views.recent import set_context_data
from image.forms import ImageForm
from image.models import Image


class UploadImageView(LoginRequiredMixin, FormView):
    form_class = ImageForm
    template_name = 'image/image_create.html'
    success_url = reverse_lazy('account:image:my_image_list')
    slug_field = 'name'
    slug_url_kwarg = 'slug'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.instance.user = self.request.user
        files = request.FILES.getlist('image_file')
        if form.is_valid():
            for f in files:
                img = Image(image_file=f, user=form.instance.user, description=form.instance.description)
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
    filterset_fields = ['date_of_upload', 'is_public', 'user']

    def get_context_data(self, **kwargs):
        context = super(ImageListView, self).get_context_data(**kwargs)
        context.update(set_context_data())
        return context


class MyImageListView(LoginRequiredMixin, ListView):
    model = Image
    paginate_by = 42
    template_name = 'image/image_list.html'
    context_object_name = 'image_list'
    ordering = '-date_of_upload'

    def get_queryset(self):
        return Image.objects.my_media(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(MyImageListView, self).get_context_data(**kwargs)
        context.update(set_context_data())
        return context


class MyImageDeleteView(LoginRequiredMixin, DeleteView):
    model = Image
    template_name = 'image/image_delete.html'
    success_url = reverse_lazy('account:my_image_list')

    def form_valid(self, form):
        if self.request.user == self.object.user:
            return super(MyImageDeleteView, self).form_valid(form)
        else:
            return self.form_invalid(form)
