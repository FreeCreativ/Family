from django import forms

from blog.models import Post, PostComment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('headline', 'content',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('comment',)
