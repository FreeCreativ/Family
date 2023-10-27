from django.urls import path

from video.views import VideoList, VideoDetail, VideoCreate, MyVideoList, UserVideoList

app_name = 'video'

urlpatterns = [
    path('', VideoList.as_view(), name='video_list'),
    path('personal/', MyVideoList.as_view(), name='my_video_list'),
    path('upload/', VideoCreate.as_view(), name='video_create'),
    path('<str:username>/', UserVideoList.as_view(), name='user_video_list'),
    path('<str:slug>', VideoDetail.as_view(), name='video_detail'),
]
