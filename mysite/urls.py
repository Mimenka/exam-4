from apps.anime.views import search_anime, search_genre
from django.contrib import admin
from django.urls import path, include
from apps.anime import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.anime.urls')),  
    path('profile/', views.user_profile, name='user_profile'),
    path('search/anime/', search_anime, name='search_anime'),
    path('search_genre/', search_genre, name='search_genre'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)