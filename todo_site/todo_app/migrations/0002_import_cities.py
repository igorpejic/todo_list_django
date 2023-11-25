# Generated by Django 4.2.7 on 2023-11-25 11:11
# This data migration will import data of cities and countries
# See: https://github.com/coderholic/django-cities


from django.db import migrations
from django.core.management import call_command


def run_cities_import(apps, schema_editor):
    call_command("cities", **{"import": "city"})


class Migration(migrations.Migration):
    dependencies = [
        ("todo_app", "0001_add_todo_model"),
        ("cities", "0011_auto_20180108_0706"),
    ]

    operations = [
        migrations.RunPython(run_cities_import),
    ]
