from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about, name='about'),    
    # path('get_almaty_boundary/', views.get_almaty_boundary, name='get_almaty_boundary') # TEST: Loading OSM data using osmnx
]
