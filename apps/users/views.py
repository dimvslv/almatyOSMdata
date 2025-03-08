from django.shortcuts import render

# Create your views here.

def auth(request):
    data = {
        'title': 'Registraton form'
    }
    return render(request, 'users/registration.html', data)