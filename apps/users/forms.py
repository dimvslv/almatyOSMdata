from django import forms
from django.contrib.auth.forms import UserCreationForm  # Форма создания пользователя Django
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm  # Форма аутентификации Django

# Создаём форму регистрации пользователя на основе класса UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    # Добавляем поле email, делаем его обязательным и задаём метку для отображения в форме
    email = forms.EmailField(required=True, label="Email")
    
    # Класс Meta в Django используется для настройки поведения класса
    class Meta:  
        model = CustomUser  
        fields = ("email", "username", "password1", "password2")
        # Перечисляем поля, которые будут отображаться в форме:
        # email — обязательный (указали выше)
        # username — остаётся, т.к. Django ожидает это поле
        # password1 и password2 — стандартные поля для ввода пароля и его подтверждения

# Создаём форму аутентификации пользователя на основе класса CustomAuthenticationForm
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))