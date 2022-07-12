import logging

from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, permissions

from core_apps.apis.menu.paginations import ReviewRatingPagination, FoodsPagination
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

    @swagger_auto_schema(
        operation_summary="List Categories",
        operation_description="""
            List Categories
        """,
        tags=["Menu"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class FoodView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    pagination_class = FoodsPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        food_name = self.request.query_params.get("food_name", None)
        if food_name is not None:
            return queryset.filter(food_name__icontains=food_name)

        category = self.request.query_params.get("category_slug")
        return queryset.filter(category__slug=category)

    @swagger_auto_schema(
        operation_summary="List Food",
        operation_description="""
            List Food by category using /?category_slug= or by food name using /?food_name=
        """,
        tags=["Menu"],
    )
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

    @swagger_auto_schema(
        operation_summary="patch review or rating",
        operation_description="""
            patch user review or rating on food post
        """,
        tags=["Menu"],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create review and rating",
        operation_description="""
            Create user review & rating on food post
        """,
        tags=["Menu"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="List ReviewRating",
        operation_description="""
            List review and rating by food name using /?by_food=
        """,
        tags=["Menu"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
