from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'visited_places_app/index.html')


def places(request):
    return render(request, 'visited_places_app/places.html')