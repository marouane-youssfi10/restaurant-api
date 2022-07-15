import logging
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from core_apps.core.orders.models import Order
from core_apps.core.payments.models import Payment

logger = logging.getLogger(__name__)


class PaymentSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField(read_only=True)
    updated_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Payment
        fields = (
            "id",
            "user",
            "method",
            "amount_paid",
            "status",
            "created_at",
            "updated_at",
        )

    def get_created_at(self, obj):
        now = obj.created_at
        formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date

    def get_updated_at(self, obj):
        then = obj.updated_at
        formatted_date = then.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data

    def _get_order_number(self, user):
        order = Order.objects.filter(user=user, is_ordered=False).latest("created_at")
        return order.order_number

    def _get_order_total_user(self, user):
        order_number = self._get_order_number(user)
        order = Order.objects.get(
            user=user, is_ordered=False, order_number=order_number
        )
        return order.order_total

    def validate(self, attrs):
        user = attrs["user"]
        # check if there's an order of this user after create a payment
        if not Order.objects.filter(
            user=user, is_ordered=False, status=Order.Statues.NEW
        ).exists():
            raise serializers.ValidationError(
                _(f"There's no Order for this user '{user}'")
            )

        return attrs

    def create(self, validated_data):
        # Store transaction details inside Payment model
        amount_paid = self._get_order_total_user(validated_data["user"])
        payment = Payment.objects.create(
            user=validated_data["user"],
            method=validated_data["method"],
            amount_paid=amount_paid,
            status=validated_data["status"],
        )
        payment.save()

        return payment
