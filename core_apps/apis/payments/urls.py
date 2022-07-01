from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core_apps.apis.payments.views import PaymentView

app_name = "payments"

router = DefaultRouter()
router.register(r"payment", PaymentView, basename="payment")


urlpatterns = [
    path("", include(router.urls)),
]
