from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from django.forms.widgets import PasswordInput, TextInput


# Create or Register user account
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# login a user
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=PasswordInput())
