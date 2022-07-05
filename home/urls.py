from django.urls import path

from .views import Index, AboutView, Search

app_name = 'home'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('search/', Search.as_view(), name='search'),
    path('about/', AboutView.as_view(), name='about'),

]
