from django.urls import path

from image.views import MyImageListView, ImageListView, MyImageDeleteView, UploadImageView, UserImageListView

app_name = 'image'

urlpatterns = [
    path('', ImageListView.as_view(), name='image_list'),
    path('upload/', UploadImageView.as_view(), name='image_create'),
    path('personal/', MyImageListView.as_view(), name='my_image_list'),
    path('<str:username>/', UserImageListView.as_view(), name='user_image_list'),
    path('<name>/delete/', MyImageDeleteView.as_view(), name='my_image_delete'),
]
