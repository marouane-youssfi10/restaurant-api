from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from core_apps.core.common.models import TimeStampedUUIDModel
from core_apps.core.menu.managers import (
    CategoryManager,
    FoodManager,
    FoodGalleryManager,
    ReviewRatingManager,
)

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
    category_image = models.ImageField(
        verbose_name=_("category image"),
        upload_to="photos/categories/",
        blank=True,
        null=True,
    )

    objects = CategoryManager()

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

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
    price = models.IntegerField(blank=False, null=False)
    category = models.ForeignKey(
        Category, verbose_name=_("category"), on_delete=models.CASCADE
    )

    objects = FoodManager()

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
        verbose_name=_("food images"), upload_to="photos/foods/", blank=True
    )

    objects = FoodGalleryManager()

    class Meta:
        verbose_name = "food gallery"
        verbose_name_plural = "food galleries"

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

    objects = ReviewRatingManager()

    class Meta:
        verbose_name = "review rating"
        verbose_name_plural = "reviews rating"

    def __str__(self):
        return f"{self.user.username} review"
