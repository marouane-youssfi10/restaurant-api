import logging

from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, permissions

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
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    @swagger_auto_schema(
        operation_summary="Create Cart",
        operation_description="""
            Create cart item
        """,
        tags=["Carts"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="List Carts",
        operation_description="""
            List carts item
        """,
        tags=["Carts"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete Cart",
        operation_description="""
            Delete carts item
        """,
        tags=["Carts"],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
