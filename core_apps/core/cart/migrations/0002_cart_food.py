# Generated by Django 3.2.11 on 2022-06-25 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cart", "0001_initial"),
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="food",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="foods",
                to="menu.food",
                verbose_name="food",
            ),
        ),
    ]
