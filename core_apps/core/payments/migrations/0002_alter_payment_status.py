# Generated by Django 3.2.11 on 2022-06-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="status",
            field=models.CharField(
                choices=[("successful", "Successful"), ("failed", "Failed")],
                max_length=20,
                verbose_name="Method payment",
            ),
        ),
    ]