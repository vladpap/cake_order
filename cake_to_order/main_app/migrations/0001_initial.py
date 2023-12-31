# Generated by Django 4.2 on 2023-07-20 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cake",
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
                ("title", models.CharField(max_length=50, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="Цена"
                    ),
                ),
                (
                    "weight",
                    models.DecimalField(
                        decimal_places=2, max_digits=2, verbose_name="Вес"
                    ),
                ),
                ("image", models.ImageField(upload_to="", verbose_name="Картинка")),
            ],
            options={
                "verbose_name": "Торт",
                "verbose_name_plural": "Торты",
            },
        ),
        migrations.CreateModel(
            name="Client",
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
                (
                    "telegram_id",
                    models.CharField(
                        db_index=True, max_length=50, verbose_name="Telegram id"
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        db_index=True,
                        max_length=128,
                        null=True,
                        region=None,
                        verbose_name="Номер телефона",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Клиент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
    ]
