from django.shortcuts import render

# Create your views here.

def users(request):
    data = {
        'title': 'Registraton form'
    }
    return render(request, 'users/registration.html', data)