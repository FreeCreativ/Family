from django.urls import path

from home.views import Index, Search, AboutView, PublicVideoDetailView, PublicVideoListView, PublicImageListView, PublicImageDetailView

app_name = 'home'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('search/', Search.as_view(), name='search'),
    path('history', AboutView.as_view(), name='about'),
    path('image', PublicImageListView.as_view(), name='image_list'),
    path('<pk>', PublicImageDetailView.as_view(), name='image_detail'),
    path('video', PublicVideoListView.as_view(), name='video_list'),
    path('<pk>', PublicVideoDetailView.as_view(), name='video_detail'),
]
