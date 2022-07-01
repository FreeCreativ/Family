from django.urls import path, include

from account.views import EducationCreateView, EducationListView, EducationDetailView, EducationUpdateView, \
    EducationDeleteView, EmailCreateView, EmailListView, EmailDetailView, EmailDeleteView, OccupationCreateView, \
    OccupationListView, OccupationDetailView, OccupationUpdateView, OccupationDeleteView, Dashboard, ProfileUpdateView, \
    AccountCreateView, UserDetailCreateView, UserListView

app_name = 'account'

edu = [
    path('new', EducationCreateView.as_view(), name='new_education'),
    path('list', EducationListView.as_view(), name='education_list'),
    path('<str:pk>', EducationDetailView.as_view(), name='education_detail'),
    path('<pk>/update', EducationUpdateView.as_view(), name='education_update'),
    path('<pk>/delete', EducationDeleteView.as_view(), name='education_delete'),
]
email = [
    path('new', EmailCreateView.as_view(), name='new_email'),
    path('list', EmailListView.as_view(), name='email_list'),
    path('<str:pk>', EmailDetailView.as_view(), name='email_detail'),
    path('<pk>/delete', EmailDeleteView.as_view(), name='email_delete'),
]
job = [
    path('new', OccupationCreateView.as_view(), name='occupation_create'),
    path('list', OccupationListView.as_view(), name='occupation_list'),
    path('<str:pk>', OccupationDetailView.as_view(), name='occupation_detail'),
    path('<pk>/update', OccupationUpdateView.as_view(), name='occupation_update'),
    path('<pk>/delete', OccupationDeleteView.as_view(), name='occupation_delete'),
]
phone = []
dash = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('update', ProfileUpdateView.as_view(), name='update'),
    path('education/', include(edu)),
    path('email/', include(email)),
    path('occuation/', include(job)),
    path('phonenumber/', include(phone)),
]
urlpatterns = [
    path('dashboard/', include(dash)),
    path('account/register/', AccountCreateView.as_view(), name='register'),
    path('account/register/continue', UserDetailCreateView.as_view(), name='r_continue'),
    path('account/list', UserListView.as_view(), name='user_list'),
]
