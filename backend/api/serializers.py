from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Place


class PlaceSerializer(GeoFeatureModelSerializer):
    """
    GeoFeatureModelSerializer will output data in a format that is GeoJSON compatible
    """
    class Meta:
        model = Place
        geo_field = "position"
        fields = ["id", "title", "address", "position"]
