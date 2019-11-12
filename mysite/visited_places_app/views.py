from django.shortcuts import render
from .models import Place
from .forms import PlaceForm
from django.views.generic import View
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'visited_places_app/index.html')


def places(request):
    user_places = Place.objects.filter(author=request.user)
    
    return render(
        request, 
        'visited_places_app/places.html',
        context={'user_places': user_places}
        )


class PlaceCreate(View):
    def get(self, request):
        place_form = PlaceForm()
        print(request.user)

        return render(
            request, 
            'visited_places_app/place_create_form.html', 
            context={'place_form': place_form})

    def post(self, request):
        bound_place_form = PlaceForm(request.POST)
        user = request.user

        if bound_place_form.is_valid():
            new_place = bound_place_form.save(user)

            return redirect('/places/', permanent=True)
        return render(
            request, 
            'visited_places_app/place_create_form.html',
            context={'place_form': bound_place_form})
