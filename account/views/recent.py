from django.views.generic.base import ContextMixin

from blog.models import Post
from image.models import Image
from video.models import Video


def set_context_data():
    latest_posts = Post.objects.order_by('-date_created')[:5]
    latest_images = Image.public.order_by('-date_of_upload')[:10]
    latest_videos = Video.public.order_by('-date_of_upload')[:10]
    context = {'latest_posts': latest_posts, 'latest_images': latest_images, 'latest_videos': latest_videos}
    return context
