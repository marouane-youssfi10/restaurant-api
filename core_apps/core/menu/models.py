from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from core_apps.core.common.models import TimeStampedUUIDModel

User = get_user_model()


class Category(TimeStampedUUIDModel):
    category_name = models.CharField(
        verbose_name=_("category name"),
        max_length=30,
        blank=False,
        null=False,
        unique=True,
    )
    slug = AutoSlugField(populate_from="category_name", always_update=True, unique=True)
    description = models.TextField(
        verbose_name=_("description"), max_length=500, blank=True
    )
    category_image = models.ImageField(upload_to="photos/categories", blank=True)

    def __str__(self):
        return self.category_name


class Food(TimeStampedUUIDModel):
    food_name = models.CharField(
        verbose_name=_("food name"), max_length=30, blank=False, null=False, unique=True
    )
    slug = AutoSlugField(populate_from="food_name", always_update=True, unique=True)
    description = models.TextField(
        verbose_name=_("description"), max_length=500, blank=True
    )
    price = models.IntegerField()
    category = models.ForeignKey(
        Category, verbose_name=_("category"), on_delete=models.CASCADE
    )

    def __str__(self):
        return self.food_name


class FoodGallery(TimeStampedUUIDModel):
    food = models.ForeignKey(
        Food,
        verbose_name=_("food"),
        related_name="food_gallery",
        on_delete=models.CASCADE,
    )
    food_images = models.ImageField(
        verbose_name=_("food images"), upload_to="photos/foods", blank=True
    )

    def __str__(self):
        return f"{self.food} gallery"


class ReviewRating(TimeStampedUUIDModel):
    user = models.ForeignKey(
        User,
        verbose_name=_("user"),
        related_name="review_rating",
        on_delete=models.CASCADE,
    )
    food = models.ForeignKey(
        Food,
        verbose_name=_("food"),
        related_name="food_review_rating",
        on_delete=models.CASCADE,
    )
    review = models.TextField(verbose_name=_("review"), max_length=500, blank=True)
    rating = models.FloatField(
        verbose_name=_("review"),
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )

    def __str__(self):
        return f"{self.user.username} review"
