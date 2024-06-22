# from django import forms

# class LoginForm(forms.Form):
#     email_or_username = forms.CharField(label='Email or Username', max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)

# forms.py

from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser
from django.conf import settings

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password")