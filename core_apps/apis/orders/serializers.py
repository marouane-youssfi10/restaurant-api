import logging

from django_countries.serializer_fields import CountryField
from django.utils.translation import gettext as _
from rest_framework import serializers, status

from core_apps.core.cart.models import Cart
from core_apps.core.orders.models import Order
from core_apps.core.orders.utils import generate_order_number

logger = logging.getLogger(__name__)


class OrderSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    updated_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "payment",
            "order_number",
            "address",
            "country",
            "city",
            "order_note",
            "order_total",
            "status",
            "is_ordered",
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

    def create(self, validated_data):
        user = validated_data["user"]
        # get all carts user
        carts = Cart.objects.filter(user=user)

        # check the cart user if empty
        cart_count = carts.count()
        if cart_count <= 0:
            logger.info(f"there's no foods in carts")
            raise serializers.ValidationError(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "detail": _("You must have one food in your cartitem at least"),
                }
            )

        # get all total price of foods
        total = 0
        for cart in carts:
            total += cart.sub_total()

        # save the order
        order = Order.objects.create(**validated_data)
        order.order_number = generate_order_number(user)
        order.order_total = total
        order.save()
        return order
