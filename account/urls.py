from django.urls import path, include

from account.views import EducationCreateView, EducationUpdateView, EducationDeleteView, \
    OccupationCreateView, OccupationDetailView, OccupationUpdateView, OccupationDeleteView, DashboardView, \
    ProfileUpdateView, AccountCreateView, UserDetailCreateView, UserListView, DiseaseDetailView, DiseaseUpdateView, \
    DiseaseDeleteView, DiseaseCreateView, BiographyUpdateView, ProfileView, Immortalised

app_name = 'account'
edu = [
    path('new', EducationCreateView.as_view(), name='new_education'),
    path('<str:pk>/update/', EducationUpdateView.as_view(), name='education_update'),
    path('<pk>/delete', EducationDeleteView.as_view(), name='education_delete'),
]

job = [
    path('new', OccupationCreateView.as_view(), name='occupation_create'),
    path('<pk>/', OccupationDetailView.as_view(), name='occupation_detail'),
    path('<pk>/update', OccupationUpdateView.as_view(), name='occupation_update'),
    path('<pk>/delete', OccupationDeleteView.as_view(), name='occupation_delete'),
]
disease = [
    path('new', DiseaseCreateView.as_view(), name='disease_create'),
    path('<str:pk>', DiseaseDetailView.as_view(), name='disease_detail'),
    path('<pk>/update', DiseaseUpdateView.as_view(), name='disease_update'),
    path('<pk>/delete', DiseaseDeleteView.as_view(), name='disease_delete'),
]
phone = []
dash = [
    path('', ProfileView.as_view(), name='profile'),
    path('settings/', ProfileUpdateView.as_view(), name='update'),
    path('update-biography/', BiographyUpdateView.as_view(), name='b-update'),
    path('education/', include(edu)),
    path('occupation/', include(job)),
    path('phonenumber/', include(phone)),
    path('disease/', include(disease)),
]
urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('register/', AccountCreateView.as_view(), name='register'),
    path('register/continue', UserDetailCreateView.as_view(), name='r_continue'),
    path('members/', UserListView.as_view(), name='user_list'),
    path('immortalised/', Immortalised.as_view(), name='late_list'),
    path('blog/', include('blog.urls')),
    path('images/', include('image.urls')),
    path('videos/', include('video.urls')),
    path('<str:username>/', include(dash)),
]
