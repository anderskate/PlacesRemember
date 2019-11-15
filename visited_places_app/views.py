from django.shortcuts import render
from .models import Place
from .forms import PlaceForm
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'visited_places_app/index.html')


@login_required
def place_detail(request, id):
    place = Place.objects.get(id=id)

    return render(
        request,
        'visited_places_app/place.html',
        context={'place': place}
        )


@login_required
def places(request):
    user_places = Place.objects.filter(author=request.user)

    return render(
        request, 
        'visited_places_app/places.html',
        context={'user_places': user_places}
        )


class PlaceCreate(LoginRequiredMixin, View):
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
