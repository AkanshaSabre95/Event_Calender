# Generated by Django 4.2.7 on 2023-11-14 05:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cal", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="end_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="event",
            name="start_date",
            field=models.DateField(),
        ),
    ]
