from django.urls import path
from .views import *

# from views import Dashboard

app_name = 'account'
urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('account/register/', RegisterUser.as_view(), name='register')
]
