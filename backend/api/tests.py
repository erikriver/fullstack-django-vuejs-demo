from django.test import TestCase
from django.contrib.gis.geos import Point
from api.models import Place


class ModelTests(TestCase):
    def testCreatePlace(self):
        """
        Test whether the Place model can save an object.
        """
        place = Place.objects.create(
            title="Hotel",
            address="near downtown",
            external_id="abc",
            position=Point(3.416061, 6.448706),
            extra={}
        )
        place.save()
