from django.urls import path
from . import views

urlpatterns = [
    path('', views.anime_list, name='anime_list'),
    path('anime/<int:anime_id>/', views.anime_detail, name='anime_detail'),
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/<int:genre_id>/', views.genre_detail, name='genre_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'), 
    path('anime/<int:anime_id>/episode/<int:episode_id>/', views.anime_detail, name='anime_detail_episode'),


]
