# Generated by Django 4.2.7 on 2023-11-16 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Airplane",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("rows", models.IntegerField()),
                ("seats_in_row", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="AirplaneType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Airport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Crew",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Route",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("distance", models.IntegerField()),
                (
                    "destination",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="routes_destination",
                        to="airport.airport",
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="routes_source",
                        to="airport.airport",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Flight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("departure_time", models.DateTimeField()),
                ("arrival_time", models.DateTimeField()),
                (
                    "airplane",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="airport.airplane",
                    ),
                ),
                ("crew", models.ManyToManyField(to="airport.crew")),
                (
                    "route",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="airport.route"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="airport.country",
                    ),
                ),
            ],
            options={
                "verbose_name": "city",
                "verbose_name_plural": "cities",
            },
        ),
        migrations.AddField(
            model_name="airport",
            name="closest_big_city",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="airport.city"
            ),
        ),
        migrations.AddField(
            model_name="airplane",
            name="airplane_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="airport.airplanetype"
            ),
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("row", models.IntegerField()),
                ("seat", models.IntegerField()),
                (
                    "flight",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="airport.flight"
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="airport.order"
                    ),
                ),
            ],
            options={
                "ordering": ["row", "seat"],
                "unique_together": {("flight", "row", "seat")},
            },
        ),
    ]
