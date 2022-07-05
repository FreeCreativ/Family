from django import forms

from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('headline', 'content',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('comment',)
