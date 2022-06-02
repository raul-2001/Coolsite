from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from players.models import *

# class AddPostFrom(forms.Form):
#     title = forms.CharField(max_length=255)
#     slug = forms.SlugField(max_length=100)
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
#     is_published = forms.BooleanField()
#     category = forms.ModelChoiceField(queryset=Category.objects.all())




class AddPostFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'The category is not choosen'

    class Meta:
        model = Player
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets= {
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }


    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 255:
            raise ValidationError("The length of symbols is more than 255")

        return title


class PlayersResitrationForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class PlayersLoginForm(AuthenticationForm):
        username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
        password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))