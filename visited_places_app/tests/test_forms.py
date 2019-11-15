from django.test import TestCase
from visited_places_app.forms import PlaceForm
from visited_places_app.models import Place
from django.contrib.auth.models import User


class TestForms(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='testuser', 
            password='12345', 
            is_active=True, 
            is_staff=True, 
            is_superuser=True
            )

    def test_place_form_valid_data(self):
        form = PlaceForm(data={
            'name': 'Test Name',
            'geom': '{"type":"Point","coordinates":[60.613976,56.832635]}',
            'comment': 'Test comment'
            })

        self.assertTrue(form.is_valid())

    def test_place_form_no_data(self):

        form = PlaceForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_place_form_save_data(self):

        form = PlaceForm(data={
            'name': 'Test Name',
            'geom': '{"type":"Point","coordinates":[60.613976,56.832635]}',
            'comment': 'Test comment'
            })
        form.is_valid()
        new_place = form.save(self.user)

        self.assertEquals(Place.objects.first().name, 'Test Name')
        self.assertEquals(
            Place.objects.first().location.json, 
            '{ "type": "Point", "coordinates": [ 60.613976, 56.832635 ] }'
        )
        self.assertEquals(Place.objects.first().comment, 'Test comment')
