from django.urls import path

from image.views import MyImageListView, ImageListView

app_name = 'image'
urlpatterns = [
    path('image', MyImageListView, name='my_image_list'),
    path('image', ImageListView, name='image_list'),
]
