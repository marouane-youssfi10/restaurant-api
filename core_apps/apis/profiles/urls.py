from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core_apps.apis.profiles.views import CustomersView

app_name = "customers"

router = DefaultRouter()
router.register(r"", CustomersView, basename="profiles")


urlpatterns = [
    path("", include(router.urls)),
]
