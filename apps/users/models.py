from django.db import models # Наследуем встроенную модель пользователя
from django.contrib.auth.models import AbstractUser # Импортируем инструменты для работы с базой данных

# Create your models here.
class CustomUser(AbstractUser): # Создаём кастомную модель пользователя на основе AbstractUser
    email = models.EmailField('Email', unique=True) # Поле email, которое будет использоваться для входа, должно быть уникальным

    USERNAME_FIELD = 'email' # Указываем, что для входа используется email вместо стандартного username
    REQUIRED_FIELDS = ['username'] # Список обязательных полей, кроме email (username оставляем для совместимости)

    def __str__(self):  # Метод строкового представления объекта пользователя
        return self.email   # Будет возвращать email пользователя

