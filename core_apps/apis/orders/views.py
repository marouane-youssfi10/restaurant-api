import logging

from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, permissions

from core_apps.apis.orders.exceptions import NoStatusInParams
from core_apps.apis.orders.serializers import OrderSerializer
from core_apps.core.orders.models import Order

User = get_user_model()

logger = logging.getLogger(__name__)


class OrderView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        status = self.request.query_params.get("status", None)
        if status is not None:
            return Order.objects.filter(user=self.request.user, status=status)

        raise NoStatusInParams

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
