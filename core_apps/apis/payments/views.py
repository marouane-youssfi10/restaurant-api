import logging

from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, permissions

from core_apps.apis.payments.serializers import PaymentSerializer
from core_apps.core.payments.models import Payment

User = get_user_model()

logger = logging.getLogger(__name__)


class PaymentView(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    @swagger_auto_schema(
        operation_summary="Create Payment",
        operation_description="""
            Create payment
        """,
        tags=["Payments"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve Payment",
        operation_description="""
            Retrieve Payment
        """,
        tags=["Payments"],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
