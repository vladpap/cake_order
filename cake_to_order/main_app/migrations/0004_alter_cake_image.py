# Generated by Django 4.2 on 2023-07-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "main_app",
            "0003_berry_cakeform_cakelevel_decor_topping_client_adress_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="cake",
            name="image",
            field=models.ImageField(upload_to="cakes_img", verbose_name="Картинка"),
        ),
    ]
