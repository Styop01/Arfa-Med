# Generated by Django 5.0.2 on 2024-02-06 19:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_iconbox_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="iconbox",
            name="description",
        ),
    ]
