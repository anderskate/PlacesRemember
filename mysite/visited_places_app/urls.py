from django.urls import path
from .views import index, places


urlpatterns = [
    path('', index, name='index_page'),
    path('places/', places, name='places'),
]