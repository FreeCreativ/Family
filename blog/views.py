from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormMixin, DeleteView

from blog.forms import *
from blog.models import *


# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'post_list'
    paginate_by = 20


class PostCreate(CreateView):
    model = Post
    template_name = 'blog/create/post.html'
    form_class = PostForm
    success_url = '/blog/'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class PostDetail(DetailView, FormMixin):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    form_class = CommentForm
    success_url = 'blog:detail'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        # context['form'] = self.form_class
        return context


class PostDelete(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = '/blog/'
    extra_context = {
        'message': 'Are you sure you want to delete this post?',
    }
