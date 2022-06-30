from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core_apps.apis.cart.views import CartView

app_name = "carts"

router = DefaultRouter()
router.register(r"cartitems", CartView, basename="cartitems")

urlpatterns = [
    path("", include(router.urls)),
]
