from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import Point
from django.db import Error
from api.models import Place

import herepy
from herepy.error import HEREError


class Command(BaseCommand):
    help = "Get places"

    def add_arguments(self, parser):
        parser.add_argument(
            "--api_key",
            default="Hq_vVaUqjEZneRMIMKDWzsZGMger-nz9sTmHzyE9Naw",
            help="HERE API key",
        )

        parser.add_argument(
            "--lat",
            # Some latitude at Berlin
            default="52.517626",
            type=float,
            help="latitude coord",
        )

        parser.add_argument(
            "--lng",
            # Some longitude at Berlin
            default="13.377864",
            type=float,
            help="longitude coord",
        )

        parser.add_argument(
            "--type",
            default="hotel",
            help="place type",
        )

    def handle(self, *args, **options):
        try:
            placesApi = herepy.PlacesApi(options["api_key"])
            places = placesApi.onebox_search(
                [options["lat"], options["lng"]], options["type"], limit=100
            )

            for place in places.items:
                title = place.pop('title')
                external_id = place.pop('id')
                address = place.pop('address')
                address = address['label']
                position = place.pop('position')
                p = Place.objects.create(
                    title=title,
                    address=address,
                    external_id=external_id,
                    position=Point(position['lat'], position['lng']),
                    extra = place
                )
                p.save()

            print(len(places.items), "places inserted")
        except HEREError:
            raise CommandError("HERE API Error")
        except Error:
            raise CommandError("Database Error")

