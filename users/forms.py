from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'col-md-12 col-sm-12'}))
    email = forms.EmailField(label='e-Mail', widget=forms.EmailInput(attrs={'class': 'col-md-12 col-sm-12'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'col-md-12 col-sm-12'}))
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput(attrs={'class': 'col-md-12 col-sm-12'}))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'col-md-12 col-sm-12'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'col-md-12 col-sm-12'}))


class UserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
