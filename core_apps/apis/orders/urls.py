from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core_apps.apis.orders.views import OrderView

app_name = "orders"

router = DefaultRouter()
router.register(r"order", OrderView, basename="order")


urlpatterns = [
    path("", include(router.urls)),
]
