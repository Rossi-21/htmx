from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name="profile"),
    path('profile/edit', views.profile_edit, name='profile-edit'),
    path('profile/delete', views.profile_delete, name="profile-delete"),
    path('<username>/', views.profile_view, name='userprofile'),
    
]