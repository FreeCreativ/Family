from django.contrib import admin

# Register your models here.
from video.models import Video, VideoComment

admin.site.register(Video)
admin.site.register(VideoComment)
