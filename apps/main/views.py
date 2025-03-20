from django.shortcuts import render
from django.http import JsonResponse
import osmnx as ox


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


# TEST: Loading OSM data using osmnx

#def get_almaty_boundary(request):
    #place_name = "Алматы, Казахстан"
    #almaty_boundary_gdf = ox.geocode_to_gdf(place_name)
    
    # Преобразуем GeoDataFrame в словарь (Python dict)
    #almaty_boundary_data = almaty_boundary_gdf.__geo_interface__

    #return JsonResponse(almaty_boundary_data, safe=False) # safe=False разрешает отдавать списки
