import logging

from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets

from core_apps.apis.payments.serializers import PaymentSerializer
from core_apps.core.payments.models import Payment

User = get_user_model()

logger = logging.getLogger(__name__)


class PaymentView(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
