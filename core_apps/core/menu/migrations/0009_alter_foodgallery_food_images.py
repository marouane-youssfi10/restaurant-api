# Generated by Django 3.2.11 on 2022-07-04 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0008_alter_category_category_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="foodgallery",
            name="food_images",
            field=models.ImageField(
                blank=True, upload_to="photos/foods/", verbose_name="food images"
            ),
        ),
    ]
