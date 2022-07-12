from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import DeleteView, BaseFormView

from blog.forms import PostForm, CommentForm
from blog.models import Post


class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'post_list'
    paginate_by = 20
    ordering = '-date_created'

    def get_queryset(self):
        return super(PostList, self).get_queryset().filter(author=self.request.user)


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/blog_create.html'
    form_class = PostForm
    success_url = '/blog/'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(PostCreate, self).form_valid(form)


class PostDetail(LoginRequiredMixin, DetailView, BaseFormView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['post_comments'] = Post.objects.get(slug=self.object.slug).postcomment_set.all()[:20]
        return context

    def get_success_url(self):
        return ''

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = self.get_object()
        form.save()
        return super(PostDetail, self).form_valid(form)


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/blog_delete.html'
    success_url = '/blog/'
    extra_context = {
        'message': 'Are you sure you want to delete this post?',
    }
