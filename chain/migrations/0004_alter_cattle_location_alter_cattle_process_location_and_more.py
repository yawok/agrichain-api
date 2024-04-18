# Generated by Django 5.0.4 on 2024-04-17 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chain", "0003_remove_location_continent_alter_location_city_and_more"),
        ("cities_light", "0011_alter_city_country_alter_city_region_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cattle",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="cities_light.city"
            ),
        ),
        migrations.AlterField(
            model_name="cattle_process",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="cities_light.city"
            ),
        ),
        migrations.AlterField(
            model_name="organisation",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="cities_light.city"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="cities_light.city"
            ),
        ),
        migrations.AlterField(
            model_name="product_process",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="cities_light.city"
            ),
        ),
    ]
