import json
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.gis.geos import Point
from api.models import Place


class ModelTests(TestCase):
    def testCreatePlace(self):
        """
        Test whether the Place model can save an object.
        """
        place = Place.objects.create(
            title="Hamburg Hotel GmbH",
            address="Hamburg Hotel GmbH, Friedrichstraße 133, 10117 Berlin, Germany",
            external_id="abc",
            position=Point(52.52357, 13.38744),
            extra={},
        )
        place.save()

        self.assertEqual(place.position.coords[0], 52.52357)
        self.assertEqual(place.position.coords[1], 13.38744)


class ApiSortingTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.places = [
            Place.objects.create(
                title="Hamburg Hotel GmbH",
                address="Berlin, Germany",
                external_id="abc",
                position=Point(52.52357, 13.38744),
                extra={},
            ),
            Place.objects.create(
                title="Adlon Kempinski Berlin",
                address="Berlin, Germany",
                external_id="abc",
                position=Point(52.51612, 13.38003),
                extra={},
            ),
            Place.objects.create(
                title="Hotel Künstlerheim Luise",
                address="Berlin, Germany",
                external_id="abc",
                position=Point(52.52172, 13.3796),
                extra={},
            ),
        ]

    def test_order_places(self):
        point_berlin = {'lat': 52.517626, 'lng': 13.377864}

        url = '/api/properties/?at=%s,%s' % (
            point_berlin['lat'], point_berlin['lng']
        )

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)

        place_list = ['Adlon Kempinski Berlin',
                      'Hotel Künstlerheim Luise', 'Hamburg Hotel GmbH']

        self.assertEqual(len(json_response['features']), len(order_list))
        for idx, place_title in enumerate(order_list):
            self.assertTrue(
                json_response['features'][idx]['properties']['title'] == place_title
            )
