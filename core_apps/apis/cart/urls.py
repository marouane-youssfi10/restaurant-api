from django.urls import path, include

from core_apps.apis.cart.views import CartView
from core_apps.utils.drf_routers import CustomRouter

app_name = "carts"

router = CustomRouter(trailing_slash=False)
router.register(r"cartitems", CartView, basename="cartitems")

urlpatterns = [
    path("", include(router.urls)),
]
