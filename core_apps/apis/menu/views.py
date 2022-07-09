import logging

from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, permissions

from core_apps.apis.menu.paginations import ReviewRatingPagination
from core_apps.apis.menu.serializers import (
    CategorySerializer,
    FoodSerializer,
    ReviewRatingSerializer,
)
from core_apps.core.menu.models import Category, Food, ReviewRating

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

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ReviewRatingView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReviewRatingSerializer
    pagination_class = ReviewRatingPagination
    queryset = ReviewRating.objects.all()

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        queryset = super().get_queryset()
        food = self.request.query_params.get("by_food")
        return queryset.filter(food__slug=food)

    def partial_update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
