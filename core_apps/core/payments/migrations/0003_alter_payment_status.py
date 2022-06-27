# Generated by Django 3.2.11 on 2022-06-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0002_alter_payment_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="status",
            field=models.CharField(
                choices=[("successful", "successful"), ("failed", "failed")],
                max_length=20,
                verbose_name="Method payment",
            ),
        ),
    ]
