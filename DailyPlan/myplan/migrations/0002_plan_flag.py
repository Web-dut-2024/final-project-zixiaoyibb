# Generated by Django 5.1.2 on 2024-11-01 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myplan", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="plan",
            name="flag",
            field=models.BooleanField(default=False),
        ),
    ]