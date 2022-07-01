import logging

from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets

from core_apps.apis.orders.serializers import OrderSerializer
from core_apps.core.orders.models import Order

User = get_user_model()

logger = logging.getLogger(__name__)


class OrderView(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
