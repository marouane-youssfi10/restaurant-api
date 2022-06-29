import logging

from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets

from core_apps.apis.menu.serializers import (
    CategorySerializer,
    FoodSerializer,
    FoodGallerySerializer,
    ReviewRatingSerializer,
)
from core_apps.core.menu.models import Category, Food, FoodGallery, ReviewRating

User = get_user_model()

logger = logging.getLogger(__name__)


class CategoryView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class FoodView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class FoodGalleryView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FoodGallerySerializer
    queryset = FoodGallery.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ReviewRatingView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ReviewRatingSerializer
    queryset = ReviewRating.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
