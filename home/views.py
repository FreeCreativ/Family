from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView

from blog.models import Post
from image.models import Image
from video.models import Video


# Create your views here.


class Index(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        latest_posts = Post.objects.order_by('-date_created')[:10]
        latest_images = Image.objects.order_by('-date_of_upload')[:10]
        latest_videos = Video.objects.order_by('-date_of_upload')[:10]
        context = super(Index, self).get_context_data()
        context['latest_posts'] = latest_posts
        context['latest_images'] = latest_images
        context['latest_videos'] = latest_videos
        return context


class Search(ListView, LoginRequiredMixin):
    template_name = 'home/search.html'
    paginate_by = 20
    context_object_name = 'result_list'

    def get_queryset(self):
        q = self.request.GET.get('q')
        result_list = [Post.objects.filter(headline__icontains=q), User.objects.filter(first_name__icontains=q)]
        return result_list


class AboutView(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        return super(AboutView, self).get_context_data()


