from django.urls import path

from home.views import Index, Search, AboutView

app_name = 'home'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('search/', Search.as_view(), name='search'),
    path('about/', AboutView.as_view(), name='about'),
]
