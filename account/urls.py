from django.urls import path
from .views import Dashboard, RegisterUser, RegisterUserDetail

# from views import Dashboard

app_name = 'account'
urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('account/register/', RegisterUser.as_view(), name='register'),
    path('account/register/continue', RegisterUserDetail.as_view(), name='r_continue'),
]
