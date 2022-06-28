from django.urls import path, include

from core_apps.apis.profiles.views import CustomersView, CustomerView
from core_apps.utils.drf_routers import CustomRouter

app_name = "customers"

router = CustomRouter(trailing_slash=False)
router.register(r"all", CustomersView, basename="profiles")
router.register(r"me", CustomerView, basename="profile")


urlpatterns = [
    path("", include(router.urls)),
]
