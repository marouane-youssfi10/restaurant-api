import logging

from rest_framework import serializers

from core_apps.core.cart.models import Cart

logger = logging.getLogger(__name__)


class CartSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField(read_only=True)
    updated_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cart
        fields = (
            "id",
            "user",
            "food",
            "quantity",
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
        if Cart.objects.filter(
            user=validated_data["user"], food=validated_data["food"]
        ).exists():
            cart = Cart.objects.get(
                user=validated_data["user"], food=validated_data["food"]
            )
            cart.quantity += validated_data["quantity"]
            cart.save()
            return cart

        return validated_data
