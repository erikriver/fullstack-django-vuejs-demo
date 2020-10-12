import json
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.gis.geos import Point
from api.models import Place, Booking


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


class PlaceSortingTest(TestCase):
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
        point_berlin = {"lat": 52.517626, "lng": 13.377864}

        url = "/api/properties/?at=%s,%s" % (point_berlin["lat"], point_berlin["lng"])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)

        place_list = [
            "Adlon Kempinski Berlin",
            "Hotel Künstlerheim Luise",
            "Hamburg Hotel GmbH",
        ]

        self.assertEqual(len(json_response), len(place_list))
        for idx, place_title in enumerate(place_list):
            self.assertTrue(json_response[idx]["title"] == place_title)


class BookingTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.place = Place.objects.create(
            title="Hamburg Hotel GmbH",
            address="Hamburg Hotel GmbH, Friedrichstraße 133, 10117 Berlin, Germany",
            external_id="abc",
            position=Point(52.52357, 13.38744),
            extra={},
        )
        self.place.save()

    def test_booking_place(self):
        data = {
            "gest_name": "Jhon Doe",
            "checkin": "2020-10-10",
            "checkout": "2020-10-20",
            "place": str(self.place.id),
        }
        response = self.client.post("/api/bookings/", data=data, format="json")
        self.assertEqual(response.status_code, 201)
        booking = Booking.objects.get(gest_name="Jhon Doe")
        self.assertEqual(booking.place, self.place)


class PlacesBookingTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.place = Place.objects.create(
            title="Hamburg Hotel GmbH",
            address="Hamburg Hotel GmbH, Friedrichstraße 133, 10117 Berlin, Germany",
            external_id="abc",
            position=Point(52.52357, 13.38744),
            extra={},
        )
        self.place.save()

    def test_get_bookings_place(self):
        data = {
            "gest_name": "Jhon Doe",
            "checkin": "2020-10-10",
            "checkout": "2020-10-20",
            "place": str(self.place.id),
        }
        response = self.client.post("/api/bookings/", data=data, format="json")
        self.assertEqual(response.status_code, 201)

        data = {
            "gest_name": "Kim Ji",
            "checkin": "2020-10-11",
            "checkout": "2020-10-21",
            "place": str(self.place.id),
        }
        response = self.client.post("/api/bookings/", data=data, format="json")
        self.assertEqual(response.status_code, 201)

        url = "/api/properties/{}/bookings/".format(str(self.place.id))

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)
        self.assertEqual(len(json_response), 2)
