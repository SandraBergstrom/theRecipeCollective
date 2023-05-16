# Based on the "Python Django Tutorial: Full-Featured Web App" tutorial by Corey Schafer
# Tutorial: https://youtu.be/UmljXZIypDc
# Snippet adapted from the tutorial with modifications

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Comment


# form that shows when user wants to register
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']


# update form that user finds on profile page
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']


# extended update form on profile page
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'food_relation', 'country']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': 'Comment'}