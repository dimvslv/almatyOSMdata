from django.urls import path
from .views import lines_geojson
from .views import points_geojson

urlpatterns = [
    path('lines/', lines_geojson, name='lines_geojson'),
    path('points/', points_geojson, name='points_geojson'),
]