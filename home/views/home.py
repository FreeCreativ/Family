from django.db.models import Q
from django.views.generic import TemplateView, ListView

from account.models import UserAccount
from blog.models import Post
from image.models import Image
from video.models import Video


# Create your views here.


class Index(TemplateView):
    template_name = 'home/index.html'


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
        video_query = Video.objects.filter(Q(description__contains=q))
        image_query = Image.objects.filter(Q(description__contains=q))
        add_query_result(post_query)
        add_query_result(user_query)
        add_query_result(image_query)
        add_query_result(video_query)
        return result_list


class AboutView(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        return super(AboutView, self).get_context_data()
