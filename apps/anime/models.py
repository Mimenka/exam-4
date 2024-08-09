from django.db import models

from utils.image_upload import upload_instance_image
from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Anime(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="No description")
    release_date = models.DateField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name='animes', blank=True)


    def __str__(self):
        return self.title

    def episodes_count(self):
        return self.episodes.count()
    episodes_count.short_description = 'Episodes Count'

class Episode(models.Model):
    anime = models.ForeignKey(Anime, related_name='episodes', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} on {self.anime.title}'

class Watchlist(models.Model):
    STATUS_CHOICES = [
        ('watching', 'Watching'),
        ('completed', 'Completed'),
        ('plan_to_watch', 'Plan to Watch'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='watchlists')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.user.username} - {self.anime.title} ({self.status})'

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='favorited_by_favorite')

    def __str__(self):
        return f'{self.user.username} - {self.anime.title}'
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    watched_anime = models.ManyToManyField(Anime, related_name='watched_by', blank=True)
    plan_to_watch_anime = models.ManyToManyField(Anime, related_name='planned_by', blank=True)
    favorite_anime = models.ManyToManyField(Anime, related_name='favorited_by', blank=True)

    def __str__(self):
        return self.user.username