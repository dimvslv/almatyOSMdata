import json
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Lines

def lines_geojson(request):
    lines = Lines.objects.using('osm_db').all()[:10000]
    geojson_str = serialize('geojson', lines, geometry_field='geom', fields=('osm_id', 'name', 'highway'))
    geojson_data = json.loads(geojson_str)  # Преобразуем строку в объект
    return JsonResponse(geojson_data, safe=False)
