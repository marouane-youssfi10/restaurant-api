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


class CategoryView(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class FoodView(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()

    def get_queryset(self):
        slug_food = self.request.query_params.get("slug_food", None)
        if slug_food is not None:
            return Food.objects.filter(slug=slug_food)

        queryset = super().get_queryset()
        category = self.request.query_params.get("category_slug")
        return queryset.filter(category__slug=category)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class FoodGalleryView(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    serializer_class = FoodGallerySerializer
    queryset = FoodGallery.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ReviewRatingView(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    serializer_class = ReviewRatingSerializer
    queryset = ReviewRating.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
