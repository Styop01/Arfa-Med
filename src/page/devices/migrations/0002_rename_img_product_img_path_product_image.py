# Generated by Django 5.0.2 on 2024-02-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="img",
            new_name="img_path",
        ),
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(default=1, upload_to="image/"),
            preserve_default=False,
        ),
    ]
