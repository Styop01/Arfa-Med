# Generated by Django 5.0.2 on 2024-02-13 19:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0012_alter_team_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="id",
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
