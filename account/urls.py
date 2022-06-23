from django.urls import path, include
from account.views import Dashboard, AccountRegistrationView, AddUserDetailView, UserListView, EditProfile, \
    EducationDetailView, EducationListView, RegisterEducationView, UpdateEducationView, DeleteEducationView

app_name = 'account'

edu = [
    path('new', RegisterEducationView.as_view(), name='new_education'),
    path('list', EducationListView.as_view(), name='education_list'),
    path('<pk>', EducationDetailView.as_view(), name='education_detail'),
    path('<pk>/update', UpdateEducationView.as_view(), name='education_update'),
    path('<pk>/delete', DeleteEducationView.as_view(), name='education_delete'),

]
email = []
job = []
phone = []
dash = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('dashboard/update', EditProfile.as_view(), name='update'),
    path('education/', include(edu)),
    path('email/', include(email)),
    path('occuation/', include(job)),
    path('phonenumber/', include(phone)),
]
urlpatterns = [
    path('dashboard/', include(dash)),
    path('account/register/', AccountRegistrationView.as_view(), name='register'),
    path('account/register/continue', AddUserDetailView.as_view(), name='r_continue'),
    path('account/list', UserListView.as_view(), name='user_list'),
]
