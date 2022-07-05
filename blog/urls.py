from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='list'),
    path('new-post/', PostCreate.as_view(), name='new_post'),
    path('<slug:slug>/', PostDetail.as_view(), name='detail'),
    path('<slug:slug>/delete', PostDelete.as_view(), name='delete'),
]
