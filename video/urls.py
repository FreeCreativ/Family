from django.urls import path

from video.views import VideoList, VideoDetail, VideoCreate

app_name = 'video'

urlpatterns = [
    path('', VideoList.as_view(), name='video_list'),
    path('upload/', VideoCreate.as_view(), name='video_create'),
    path('<str:slug>', VideoDetail.as_view(), name='video_detail'),
]
