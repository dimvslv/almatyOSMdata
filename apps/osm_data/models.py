# для подключения готовой бд формируем этот файл командой
# python manage.py inspectdb --database osm_db

from django.contrib.gis.db import models


class Lines(models.Model):
    osm_id = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    highway = models.CharField(blank=True, null=True)
    waterway = models.CharField(blank=True, null=True)
    aerialway = models.CharField(blank=True, null=True)
    barrier = models.CharField(blank=True, null=True)
    man_made = models.CharField(blank=True, null=True)
    railway = models.CharField(blank=True, null=True)
    z_order = models.IntegerField(blank=True, null=True)
    other_tags = models.CharField(blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lines'


class Multilinestrings(models.Model):
    osm_id = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    other_tags = models.CharField(blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'multilinestrings'


class Multipolygons(models.Model):
    osm_id = models.CharField(blank=True, null=True)
    osm_way_id = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    aeroway = models.CharField(blank=True, null=True)
    amenity = models.CharField(blank=True, null=True)
    admin_level = models.CharField(blank=True, null=True)
    barrier = models.CharField(blank=True, null=True)
    boundary = models.CharField(blank=True, null=True)
    building = models.CharField(blank=True, null=True)
    craft = models.CharField(blank=True, null=True)
    geological = models.CharField(blank=True, null=True)
    historic = models.CharField(blank=True, null=True)
    land_area = models.CharField(blank=True, null=True)
    landuse = models.CharField(blank=True, null=True)
    leisure = models.CharField(blank=True, null=True)
    man_made = models.CharField(blank=True, null=True)
    military = models.CharField(blank=True, null=True)
    natural = models.CharField(blank=True, null=True)
    office = models.CharField(blank=True, null=True)
    place = models.CharField(blank=True, null=True)
    shop = models.CharField(blank=True, null=True)
    sport = models.CharField(blank=True, null=True)
    tourism = models.CharField(blank=True, null=True)
    other_tags = models.CharField(blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'multipolygons'


class OtherRelations(models.Model):
    osm_id = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    other_tags = models.CharField(blank=True, null=True)
    geom = models.GeometryCollectionField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_relations'


class Points(models.Model):
    osm_id = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    barrier = models.CharField(blank=True, null=True)
    highway = models.CharField(blank=True, null=True)
    ref = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    is_in = models.CharField(blank=True, null=True)
    place = models.CharField(blank=True, null=True)
    man_made = models.CharField(blank=True, null=True)
    other_tags = models.CharField(blank=True, null=True)
    geom = models.MultiPointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'points'

    def __str__(self):
        return self.name if self.name else f"Line {self.id}"
