from django.contrib import admin

from .models import PostComment, Post


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("headline",)}


# Register your models here.
admin.site.register(Post)
admin.site.register(PostComment)
