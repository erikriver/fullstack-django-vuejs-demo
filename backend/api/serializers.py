from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Place, Booking


class PlaceSerializer(GeoFeatureModelSerializer):
    """
    GeoFeatureModelSerializer will output data in a format that is GeoJSON compatible
    """
    class Meta:
        model = Place
        geo_field = "position"
        fields = ["id", "title", "address", "position"]


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ["gest_name", "checkin", "checkout", "place"]

    def create(self, validated_data):
        return Booking.objects.create(**validated_data)
