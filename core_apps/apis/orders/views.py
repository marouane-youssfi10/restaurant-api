import logging

from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from rest_framework import mixins, permissions, viewsets

from core_apps.apis.menu.exceptions import OrderDoesNotExist
from core_apps.apis.orders.exceptions import NoStatusInParams
from core_apps.apis.orders.serializers import OrderSerializer
from core_apps.core.orders.models import Order

User = get_user_model()

logger = logging.getLogger(__name__)


class OrderView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()

    def get_object(self):
        try:
            return Order.objects.get(pkid=self.kwargs["pk"])
        except Order.DoesNotExist:
            raise OrderDoesNotExist

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get("status", None)
        if status is not None:
            return queryset.filter(user=self.request.user, status=status)

        raise NoStatusInParams

    @swagger_auto_schema(
        operation_summary="Create Order",
        operation_description="""
            Create order
        """,
        tags=["Orders"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Patch Order",
        operation_description="""
            Patch order status
        """,
        tags=["Orders"],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="List Order",
        operation_description="""
            List order bu status using /?status=
        """,
        tags=["Orders"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
