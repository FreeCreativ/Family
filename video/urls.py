from django.urls import path

from video.views import VideoList, VideoDetail

app_name = 'video'

urlpatterns = [
    path('', VideoList.as_view(), name='video_list'),
    path('<str:slug>', VideoDetail.as_view(), name='video_detail'),
]
