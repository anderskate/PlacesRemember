from django.urls import path
from .views import index, places, PlaceCreate


urlpatterns = [
    path('', index, name='index_page'),
    path('places/', places, name='places'),
    path('create_place/', PlaceCreate.as_view(), name='create_place')
]