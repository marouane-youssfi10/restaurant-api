# Generated by Django 3.2.11 on 2022-07-04 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0006_alter_category_category_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="category_image",
            field=models.ImageField(
                blank=True,
                upload_to="photos/categories/",
                verbose_name="category image",
            ),
        ),
    ]