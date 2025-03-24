import json
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Lines
from .models import Points

def lines_geojson(request):
    lines = Lines.objects.using('osm_db').filter(highway__in=['primary', 'secondary'])
    geojson_str = serialize('geojson', lines, geometry_field='geom', fields=('osm_id', 'name', 'highway'))
    geojson_data = json.loads(geojson_str)  # Преобразуем строку в объект
    
    return JsonResponse(geojson_data, safe=False)

def points_geojson(request):
    points = Points.objects.using('osm_db').filter(highway='bus_stop')[:500]
    geojson_str = serialize('geojson', points, geometry_field='geom', fields=('osm_id', 'name', 'highway'))
    geojson_data = json.loads(geojson_str)

    return JsonResponse(geojson_data, safe=False)


