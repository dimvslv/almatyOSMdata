from django.shortcuts import render

# Create your views here.

# Django автоматически ищет шаблоны в папках, указанных в настройках TEMPLATES['DIRS'], 
# а также внутри папок templates каждого установленного приложения.
# Здесь 'main' — это путь к файлу шаблона, который Django попытается найти в этих директориях.
def index(request):
    data = {
        'title': 'OpenStreetMap layers for Almaty'
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')