# Generated by Django 3.1.2 on 2020-10-11 05:44

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=500)),
                ("external_id", models.CharField(max_length=255)),
                ("address", models.TextField()),
                ("position", django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ("extra", models.JSONField()),
            ],
            options={
                "ordering": ("title",),
            },
        ),
    ]
