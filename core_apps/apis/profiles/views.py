import logging

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
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomersSerializer
    queryset = Customer.objects.all()
    renderer_classes = (CustomersJSONRenderer,)
    pagination_class = CustomersPagination

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
