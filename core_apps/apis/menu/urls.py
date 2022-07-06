from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core_apps.apis.menu.views import (
    CategoryView,
    FoodView,
    ReviewRatingView,
)

app_name = "menu"

router = DefaultRouter()
router.register(r"categories", CategoryView, basename="categories")
router.register(r"foods", FoodView, basename="foods")
router.register(r"review-rating", ReviewRatingView, basename="review-rating")


urlpatterns = [
    path("", include(router.urls)),
]
