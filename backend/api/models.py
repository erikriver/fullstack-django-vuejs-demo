import uuid
from django.contrib.gis.db import models


class Place(models.Model):
    """
    A place in a city
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500)
    external_id = models.CharField(max_length=255)
    address = models.TextField()
    position = models.PointField(srid=4326)  # WGS 84 projection
    extra = models.JSONField()

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return "{} ({:f}, {:f})".format(self.title, self.position.x, self.position.y)
