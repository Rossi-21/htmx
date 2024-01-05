from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/create/', views.post_create_view, name="post-create"),
    path('post/delete/<pk>/', views.post_delete_view, name="post-delete"),
]