# Generated by Django 5.0.1 on 2024-02-06 19:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "contact_us",
            "0003_alter_card_icon_alter_card_subtitle_alter_card_title_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="form",
            name="icon",
            field=models.CharField(max_length=20),
        ),
    ]
