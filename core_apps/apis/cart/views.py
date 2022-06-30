import logging

from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets

from core_apps.apis.cart.serializers import CartSerializer
from core_apps.core.cart.models import Cart

User = get_user_model()

logger = logging.getLogger(__name__)


class CartView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
