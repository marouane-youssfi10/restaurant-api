# Generated by Django 3.2.11 on 2022-07-02 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0003_auto_20220630_2207"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="category_image",
            field=models.ImageField(upload_to="photos/categories"),
        ),
    ]
