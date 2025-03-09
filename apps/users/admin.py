from django.contrib import admin # Импортируем модуль для работы с админкой
from django.contrib.auth.admin import UserAdmin # Импортируем встроенный класс админки для пользователей
from django.contrib.auth import get_user_model # Функция, которая получает текущую модель пользователя

# Register your models here.

# Получаем модель пользователя, указанную в settings.py -> AUTH_USER_MODEL
User = get_user_model() # Теперь User ссылается на CustomUser из users/models.py

# Регистрируем модель пользователя в админке

@admin.register(User) 
# Декоратор @admin.register(User) "прикрепляет" класс CustomUserAdmin к модели User. 
# Декоратор @admin.register(User) работает только на класс, который идёт сразу после него.
# Эквивалентно admin.site.register(User, CustomUserAdmin).

class CustomUserAdmin(UserAdmin): # Используем встроенный UserAdmin для управления пользователями
    pass # Здесь можно добавить кастомные настройки для отображения пользователей в админке