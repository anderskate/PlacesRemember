from django.contrib import admin
from visited_places_app.models import Place
from leaflet.admin import LeafletGeoAdmin


class PlaceAdmin(LeafletGeoAdmin):
    list_display = ['name', 'location']

admin.site.register(Place, PlaceAdmin)