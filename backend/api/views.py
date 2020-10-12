from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from .serializers import PlaceSerializer, BookingSerializer
from .models import Place, Booking


class PlaceViewSet(viewsets.ModelViewSet):
    """
    Viewset for Place objects around Lat/Lon
    url: /api/properties?at=LAT,LONG
    """

    serializer_class = PlaceSerializer

    def get_queryset(self):
        point_string = self.request.query_params.get("at", None)
        try:
            (x, y) = (float(n) for n in point_string.split(","))
        except ValueError:
            raise ParseError("Invalid geometry string supplied for parameter `at`")

        point = Point(x, y, srid=4326)

        # only return last 10 around Lat/Lon
        return Place.objects.annotate(distance=Distance("position", point)).order_by(
            "distance"
        )[0:10]


class BookingViewSet(viewsets.ModelViewSet):
    """
    Viewset creates a booking for a property
    url: /api/bookings

    TODO:
        permission_classes = [permissions.IsAuthenticated]
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class PlaceBookingViewSet(viewsets.ModelViewSet):
    """
    Viewset returns the bookings for a property
    url: /api/properties/PROPERTY_ID/bookings

    TODO:
        permission_classes = [permissions.IsAuthenticated]
    """
    serializer_class = BookingSerializer

    def get_queryset(self):
        place_id = self.kwargs['property_id']
        return Booking.objects.filter(place__id=place_id)