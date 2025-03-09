from django.shortcuts import render, redirect # Функции для рендеринга шаблонов и перенаправления
from .forms import CustomUserCreationForm # Импортируем кастомную форму регистрации созданную в forms.py

# Create your views here.

def register(request): # Определяем представление (view) для регистрации пользователей    
    if request.method == "POST":  # Проверяем, был ли отправлен POST-запрос (т.е. пользователь отправил форму)
        register_form = CustomUserCreationForm(request.POST)  # Создаём объект формы и заполняем его данными из запроса
        if register_form.is_valid():  # Проверяем, прошла ли форма валидацию (корректные ли данные введены)
            register_form.save()  # Если форма валидна, сохраняем нового пользователя в базе данных
            return redirect("login")  # После успешной регистрации перенаправляем пользователя на страницу входа
    else: # Если это GET-запрос (пользователь просто открывает страницу)
        register_form = CustomUserCreationForm()

    context = {
        "register_form": register_form,
        "title": 'Registration form'
    }

    return render(request, 'users/registration.html', context)
    # Отправляем HTML-шаблон и передаём в него объект формы, чтобы пользователь мог заполнить её

    # Функция render() принимает четыре аргумента:
    # request — объект запроса.
    # "users/registration.html" — путь к HTML-шаблону, который нужно отобразить.
    # {"register_form": form} — Имя, формы созданной в переменной form, которое передаётся в шаблон.
    # data — текст для отображения заголовка в HTML-шаблоне