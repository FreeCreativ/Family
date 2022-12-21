from django.db.models import Q
from django.views.generic import TemplateView, ListView

from account.models import UserAccount
from account.views.recent import set_context_data
from blog.models import Post
from image.models import Image
from video.models import Video


# Create your views here.


class Index(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        latest_posts = Post.objects.order_by('-date_created')[:5]
        latest_images = Image.public.order_by('-date_of_upload')[:10]
        latest_videos = Video.public.order_by('-date_of_upload')[:10]
        context = super(Index, self).get_context_data()
        context['latest_posts'] = latest_posts
        context['latest_images'] = latest_images
        context['latest_videos'] = latest_videos
        return context


class Search(ListView):
    template_name = 'home/search.html'
    paginate_by = 20
    context_object_name = 'result_list'

    def get_queryset(self):
        result_list = []
        q = self.request.GET.get('q')

        def add_query_result(result):
            if result.count() != 0:
                return result_list.append(result)

        post_query = Post.objects.filter(Q(headline__contains=q) | Q(content__contains=q))
        user_query = UserAccount.objects.filter(
            Q(first_name__icontains=q) | Q(middle_name__icontains=q) | Q(last_name__icontains=q) | Q(
                username__icontains=q))
        add_query_result(post_query)
        add_query_result(user_query)
        return result_list

    def get_context_data(self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        context.update(set_context_data())
        return context


class AboutView(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        return super(AboutView, self).get_context_data()
