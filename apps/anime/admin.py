from django.contrib import admin
from django.utils.html import format_html
from .models import Anime, Episode, Genre, Review, Favorite, Watchlist

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'release_date', 'episodes_count', 'rating']
    inlines = [EpisodeInline]
    filter_horizontal = ('genres',)  

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['title', 'anime', 'video_file', 'video_player']
    
    def video_player(self, obj):
        if obj.video_file:
            return format_html(
                '<video width="320" height="240" controls>'
                '<source src="{0}" type="video/mp4">'
                'Your browser does not support the video tag.'
                '</video>',
                obj.video_file.url
            )
        return "No Video"
    video_player.short_description = 'Video Preview'

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['anime', 'user', 'rating', 'comment', 'created_at']

@admin.register(Watchlist)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ['user', 'anime', 'status']

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'anime']
