# Generated by Django 3.2.11 on 2022-06-25 17:29

import autoslug.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category_name",
                    models.CharField(
                        max_length=30, unique=True, verbose_name="category name"
                    ),
                ),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        always_update=True,
                        editable=False,
                        populate_from="category_name",
                        unique=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=500, verbose_name="description"
                    ),
                ),
                (
                    "category_image",
                    models.ImageField(blank=True, upload_to="photos/categories"),
                ),
            ],
            options={
                "ordering": ["-created_at", "-updated_at"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Food",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "food_name",
                    models.CharField(
                        max_length=30, unique=True, verbose_name="food name"
                    ),
                ),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        always_update=True,
                        editable=False,
                        populate_from="food_name",
                        unique=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=500, verbose_name="description"
                    ),
                ),
                ("price", models.IntegerField()),
            ],
            options={
                "ordering": ["-created_at", "-updated_at"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="FoodGallery",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "food_images",
                    models.ImageField(
                        blank=True, upload_to="photos/foods", verbose_name="food images"
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at", "-updated_at"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ReviewRating",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "review",
                    models.TextField(blank=True, max_length=500, verbose_name="review"),
                ),
                (
                    "rating",
                    models.FloatField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="review",
                    ),
                ),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="food_review_rating",
                        to="menu.food",
                        verbose_name="food",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at", "-updated_at"],
                "abstract": False,
            },
        ),
    ]
