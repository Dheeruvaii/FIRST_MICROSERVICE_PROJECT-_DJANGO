# Generated by Django 5.0.1 on 2024-02-04 08:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_auth", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FavoriteProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField()),
                ("product_id", models.IntegerField()),
            ],
        ),
    ]
