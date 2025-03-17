from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # алиас для обращения к LoginView и LogoutView
from .views import CustomLoginView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(template_name='users/login.html', next_page='main'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='main'), name='logout'),
]
