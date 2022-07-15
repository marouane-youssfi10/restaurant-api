import logging

from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, permissions

from core_apps.apis.profiles.paginations import CustomersPagination
from core_apps.apis.profiles.renderers import (
    CustomersJSONRenderer,
)
from core_apps.apis.profiles.serializers import CustomersSerializer
from core_apps.core.profiles.models import Customer

User = get_user_model()

logger = logging.getLogger(__name__)


class CustomersView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CustomersSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Customer.objects.all()
    renderer_classes = (CustomersJSONRenderer,)
    pagination_class = CustomersPagination

    @swagger_auto_schema(
        operation_summary="Retrieve Customer",
        operation_description="""
            Retrieve customer profile
        """,
        tags=["Profiles"],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Patch Customer",
        operation_description="""
            Patch customer profile
        """,
        tags=["Profiles"],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update Customer",
        operation_description="""
            Update customer profile
        """,
        tags=["Profiles"],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
