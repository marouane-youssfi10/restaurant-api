import logging

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import mixins, viewsets, permissions
from rest_framework.exceptions import NotFound

from core_apps.apis.profiles.paginations import CustomersPagination
from core_apps.apis.profiles.renderers import (
    CustomersJSONRenderer,
    CustomerJSONRenderer,
)
from core_apps.apis.profiles.serializers import CustomersSerializer
from core_apps.core.profiles.models import Customer

User = get_user_model()

logger = logging.getLogger(__name__)


class MyCustomMixin(object):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomersSerializer


class CustomersView(MyCustomMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    renderer_classes = (CustomersJSONRenderer,)
    pagination_class = CustomersPagination

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CustomerView(
    MyCustomMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    renderer_classes = (CustomerJSONRenderer,)

    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        try:
            User.object.get(user=self.get_object())
        except ObjectDoesNotExist:
            logger.info("A Customer profile with this user does not exist")
            raise NotFound("A Customer profile with this user does not exist")

        return super().retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
