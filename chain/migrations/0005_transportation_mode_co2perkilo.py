# Generated by Django 5.0.4 on 2024-04-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chain", "0004_alter_cattle_location_alter_cattle_process_location_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="transportation_mode",
            name="co2perkilo",
            field=models.DecimalField(
                decimal_places=4,
                default=0,
                max_digits=7,
                null=True,
                verbose_name="Carbon Emission per Kilometer",
            ),
        ),
    ]