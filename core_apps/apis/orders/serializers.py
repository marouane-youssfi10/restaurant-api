import logging

from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from core_apps.apis.orders.exceptions import CartItemIsEmpty, HaveMoreOrders
from core_apps.core.cart.models import Cart
from core_apps.core.orders.models import Order
from core_apps.utils.generators import generate_order_number

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

    def _get_all_foods_prices(self, user):
        carts = Cart.objects.filter(user=user)
        # get all total price of foods
        total = 0
        for cart in carts:
            total += cart.sub_total()

        return total

    def validate(self, attrs):
        # check status in request post is exists to update
        if "status" in self.initial_data:
            return attrs

        # check if there's more than 1 orders user
        user = attrs["user"]
        if Order.objects.filter(user=user, status=Order.Statues.NEW).count() >= 1:
            raise HaveMoreOrders

        # check if cart user is empty
        if Cart.objects.filter(user=user).count() <= 0:
            raise CartItemIsEmpty

        return attrs

    def create(self, validated_data):
        total_price = self._get_all_foods_prices(validated_data["user"])
        # create order
        order = Order.objects.create(**validated_data)
        order.order_number = generate_order_number()
        order.order_total = total_price
        order.save()

        return order

    def update(self, instance, validated_data):
        order = Order.objects.get(user=instance.user, order_number=instance)
        order.status = validated_data["status"]
        order.save()

        return order
