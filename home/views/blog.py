from django.views.generic import ListView, DetailView
from django.views.generic.edit import BaseFormView

from blog.forms import CommentForm
from blog.models import Post


class PublicPostList(ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'post_list'
    paginate_by = 20
    ordering = '-date_created'


class PublicPostDetail(DetailView, BaseFormView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(PublicPostDetail, self).get_context_data(**kwargs)
        context['post_comments'] = Post.objects.get(slug=self.object.slug).postcomment_set.all()[:50]
        return context

    def get_success_url(self):
        return ''

    def form_valid(self, form):
        if self.request.user:
            form.instance.user = self.request.user
            form.instance.post = self.get_object()
            form.save()
            return super(PublicPostDetail, self).form_valid(form)
        else:
            form.instance.user = 'anonymous'
            form.instance.post = self.get_object()
            form.save()
            return super(PublicPostDetail, self).form_valid(form)
