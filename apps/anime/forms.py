from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import UserProfile, Anime


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    pass
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['watched_anime', 'plan_to_watch_anime', 'favorite_anime']
        widgets = {
            'watched_anime': forms.CheckboxSelectMultiple(),
            'plan_to_watch_anime': forms.CheckboxSelectMultiple(),
            'favorite_anime': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['watched_anime'].queryset = Anime.objects.all()
            self.fields['plan_to_watch_anime'].queryset = Anime.objects.all()
            self.fields['favorite_anime'].queryset = Anime.objects.all()