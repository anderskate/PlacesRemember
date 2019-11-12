from django.urls import path
from .views import index, places, place_detail, PlaceCreate


urlpatterns = [
    path('', index, name='index_page'),
    path('place/create/', PlaceCreate.as_view(), name='create_place'),
    path('place/<str:id>/', place_detail, name='place_detail_url'),
    path('places/', places, name='places'),
]