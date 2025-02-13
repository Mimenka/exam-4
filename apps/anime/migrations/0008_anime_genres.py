# Generated by Django 4.2.13 on 2024-08-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("anime", "0007_alter_userprofile_favorite_anime"),
    ]

    operations = [
        migrations.AddField(
            model_name="anime",
            name="genres",
            field=models.ManyToManyField(
                blank=True, related_name="animes", to="anime.genre"
            ),
        ),
    ]
