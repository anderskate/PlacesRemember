from django.test import TestCase, Client
from django.urls import reverse
from visited_places_app.models import Place
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class TestViewsWhenUserIsAuthorized(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='testuser', 
            password='12345', 
            is_active=True, 
            is_staff=True, 
            is_superuser=True
            )
        self.user.set_password('hello')
        self.user.save()
        self.user = authenticate(username='testuser', password='hello')
        login = self.client.login(username='testuser', password='hello')

        self.places_url = reverse('places')
        self.create_place_url = reverse('create_place')
        

    def test_places_GET(self):

        response = self.client.get(self.places_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'visited_places_app/places.html')

    def test_create_place_GET(self):

        response = self.client.get(self.create_place_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'visited_places_app/place_create_form.html')

    def test_create_place_POST_adds_new_place(self):

        response = self.client.post(self.create_place_url, {
            'name': ['Test Place'],
            'geom': ['{"type":"Point","coordinates":[60.612946,56.830756]}'],
            'comment': ['Test comment']
            })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Place.objects.first().name, 'Test Place')

    def test_create_place_POST_no_data(self):

        response = self.client.post(self.create_place_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Place.objects.count(), 0)


class TestViewsWhenUserIsNotAuthorized(TestCase):

    def setUp(self):
        self.client = Client()

        self.places_url = reverse('places')
        self.create_place_url = reverse('create_place')

    def test_places_GET(self):

        response = self.client.get(self.places_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.context, None)

    def test_create_place_GET(self):

        response = self.client.get(self.create_place_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.context, None)

    def test_create_place_POST_adds_new_place(self):

        response = self.client.post(self.create_place_url, {
            'name': ['Test Place'],
            'geom': ['{"type":"Point","coordinates":[60.612946,56.830756]}'],
            'comment': ['Test comment']
            })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.context, None)

    def test_create_place_POST_no_data(self):

        response = self.client.post(self.create_place_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.context, None)


