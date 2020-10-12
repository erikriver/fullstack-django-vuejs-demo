from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Place, Booking


class PlaceSerializer(ModelSerializer):
    """
    GeoFeatureModelSerializer will output data in a format that is GeoJSON compatible
    """

    location = SerializerMethodField()

    class Meta:
        model = Place
        fields = ["id", "title", "address", "location"]

    def get_location(self, obj):
        return "{:f},{:f}".format(obj.position.x, obj.position.y)


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ["gest_name", "checkin", "checkout", "place"]

    def create(self, validated_data):
        return Booking.objects.create(**validated_data)
