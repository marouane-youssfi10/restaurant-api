import logging

from rest_framework import serializers

from core_apps.core.cart.models import Cart
from core_apps.core.orders.models import OrderItem, Order
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

    def _order_number(self, user):
        order = Order.objects.filter(user=user, is_ordered=False).latest("created_at")
        return order.order_number

    def _order_total_user(self, user):
        order_number = self._order_number(user)
        order = Order.objects.get(
            user=user, is_ordered=False, order_number=order_number
        )
        return order, order.order_total

    def create(self, validated_data):
        user = validated_data["user"]
        method = validated_data["method"]
        status = validated_data["status"]

        # Store transaction details inside Payment model
        order, amount_paid = self._order_total_user(user)
        payment = Payment.objects.create(
            user=user, method=method, amount_paid=amount_paid, status=status
        )
        payment.save()

        # update payment & status & is_ordered in order table
        order.payment = payment
        order.is_ordered = True
        order.status = Order.Gender.ACCEPTED
        order.save()

        # Move the cart items to OrderItem table
        cart_items = Cart.objects.filter(user=user)
        for item in cart_items:
            order_item = OrderItem.objects.create(
                user=order.user,
                payment=payment,
                order=order,
                food=item.food,
                quantity=item.quantity,
                food_price=item.food.price,
                ordered=True,
            )
            order_item.save()

        # Clear cart
        Cart.objects.filter(user=user).delete()

        return payment
