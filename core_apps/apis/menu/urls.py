from django.urls import path, include

from core_apps.apis.menu.views import (
    CategoryView,
    FoodView,
    FoodGalleryView,
    ReviewRatingView,
)
from core_apps.utils.drf_routers import CustomRouter

app_name = "menu"

router = CustomRouter(trailing_slash=False)
router.register(r"categories", CategoryView, basename="categories")
router.register(r"foods", FoodView, basename="foods")
router.register(r"food-gallery", FoodGalleryView, basename="food-gallery")
router.register(r"review-rating", ReviewRatingView, basename="review-rating")


urlpatterns = [
    path("", include(router.urls)),
]
