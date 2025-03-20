from django.urls import path
from .views import lines_geojson

urlpatterns = [
    path('lines/', lines_geojson, name='lines_geojson'),
]