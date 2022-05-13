from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from main.models import *


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Введите Имя"}))
    email = forms.EmailField(max_length=254, required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Введите Email"}))
    password1 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Введите Пароль"}))
    password2 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Повторите Пароль"}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class Confirmation(forms.ModelForm):
    verification_code = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Введите код подтверждения", 'type': 'number'}))

    class Meta:
        model = User
        fields = [
            'verification_code',
        ]


class Login_Form(forms.Form):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Введите Имя или Email"}))
    password1 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Введите Пароль"}))

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
        ]
