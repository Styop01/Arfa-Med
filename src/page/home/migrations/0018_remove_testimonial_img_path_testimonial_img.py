# Generated by Django 5.0.2 on 2024-02-16 19:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0017_remove_clients_img_path_clients_img"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="testimonial",
            name="img_path",
        ),
        migrations.AddField(
            model_name="testimonial",
            name="img",
            field=models.ImageField(default=1, upload_to="images/"),
            preserve_default=False,
        ),
    ]
