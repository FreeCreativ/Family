from django.urls import path, include

from account.views import EducationCreateView, EducationListView, EducationDetailView, EducationUpdateView, \
    EducationDeleteView, EmailCreateView, EmailListView, EmailDetailView, EmailDeleteView, OccupationCreateView, \
    OccupationListView, OccupationDetailView, OccupationUpdateView, OccupationDeleteView, DashboardView, \
    ProfileUpdateView, \
    AccountCreateView, UserDetailCreateView, UserListView, DiseaseDetailView, DiseaseUpdateView, DiseaseDeleteView, \
    DiseaseCreateView, DiseaseListView, ProfilePictureUpdateView, BiographyUpdateView, ProfileView

app_name = 'account'
edu = [
    path('', EducationListView.as_view(), name='education_list'),
    path('new', EducationCreateView.as_view(), name='new_education'),
    path('<str:pk>', EducationDetailView.as_view(), name='education_detail'),
    path('<pk>/update', EducationUpdateView.as_view(), name='education_update'),
    path('<pk>/delete', EducationDeleteView.as_view(), name='education_delete'),
]
email = [
    path('', EmailListView.as_view(), name='email_list'),
    path('new', EmailCreateView.as_view(), name='new_email'),
    path('<str:pk>', EmailDetailView.as_view(), name='email_detail'),
    path('<pk>/delete', EmailDeleteView.as_view(), name='email_delete'),
]
job = [
    path('', OccupationListView.as_view(), name='occupation_list'),
    path('new', OccupationCreateView.as_view(), name='occupation_create'),
    path('<str:pk>', OccupationDetailView.as_view(), name='occupation_detail'),
    path('<pk>/update', OccupationUpdateView.as_view(), name='occupation_update'),
    path('<pk>/delete', OccupationDeleteView.as_view(), name='occupation_delete'),
]
disease = [
    path('', DiseaseListView.as_view(), name='disease_list'),
    path('new', DiseaseCreateView.as_view(), name='disease_create'),
    path('<str:pk>', DiseaseDetailView.as_view(), name='disease_detail'),
    path('<pk>/update', DiseaseUpdateView.as_view(), name='disease_update'),
    path('<pk>/delete', DiseaseDeleteView.as_view(), name='disease_delete'),
]
phone = []
dash = [
    path('', ProfileView.as_view(), name='profile'),
    path('update', ProfileUpdateView.as_view(), name='update'),
    path('update-picture', ProfilePictureUpdateView.as_view(), name='p-update'),
    path('update-biography', BiographyUpdateView.as_view(), name='b-update'),
    path('education/', include(edu)),
    path('email/', include(email)),
    path('occupation/', include(job)),
    path('phonenumber/', include(phone)),
    path('disease/', include(phone)),
]
urlpatterns = [
    path('account/dashboard/', DashboardView.as_view(), name='dashboard'),
    path('account/register/', AccountCreateView.as_view(), name='register'),
    path('account/register/continue', UserDetailCreateView.as_view(), name='r_continue'),
    path('account/list', UserListView.as_view(), name='user_list'),
    path('account/<str:username>/', include(dash)),
    path('blog/', include('blog.urls')),
    path('images/', include('image.urls')),
]
