from django.urls import path

from image.views import MyImageListView, ImageListView, MyImageDeleteView

app_name = 'image'

urlpatterns = [
    path('', ImageListView.as_view(), name='image_list'),
    path('my-images', MyImageListView.as_view(), name='my_image_list'),
    path('<pk>/delete', MyImageDeleteView.as_view(), name='my_image_delete'),
]
