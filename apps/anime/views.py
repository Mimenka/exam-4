from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout
from apps.anime.models import Genre, Anime, Episode, UserProfile
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm
from django.contrib.auth.decorators import login_required


def anime_list(request):
    animes = Anime.objects.all()
    return render(request, 'anime/anime_list.html', {'animes': animes})

def anime_detail(request, anime_id, episode_id=None):
    anime = get_object_or_404(Anime, id=anime_id)
    if episode_id:
        selected_episode = get_object_or_404(Episode, id=episode_id)
    else:
        selected_episode = anime.episodes.first()  

    return render(request, 'anime/anime_detail.html', {
        'anime': anime,
        'selected_episode': selected_episode,
    })


def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'anime/genre_list.html', {'genres': genres})

def genre_detail(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    animes = genre.animes.all() 
    return render(request, 'anime/genre_detail.html', {'genre': genre, 'animes': animes})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form.get_user())
            return redirect('anime_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'anime/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('anime_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'anime/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('anime_list')


@login_required
def user_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=profile, user=request.user)
    
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'anime/profile.html', context)

def search_anime(request):
    query = request.GET.get('q')
    if query:
        results = Anime.objects.filter(title__icontains=query)
    else:
        results = Anime.objects.none()

    return render(request, 'anime/search_results.html', {'results': results, 'query': query})

def search_genre(request):
    query = request.GET.get('q')
    if query:
        results = Genre.objects.filter(name__icontains=query)
    else:
        results = Genre.objects.none() 

    return render(request, 'anime/search_genre_results.html', {'results': results, 'query': query})