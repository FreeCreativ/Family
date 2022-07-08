from django.urls import path

from blog.views import PostList, PostCreate, PostDetail, PostDelete

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='blog_list'),
    path('new-post/', PostCreate.as_view(), name='blog_create'),
    path('<slug:slug>/', PostDetail.as_view(), name='blog_detail'),
    path('<slug:slug>/delete', PostDelete.as_view(), name='blog_delete'),
]
