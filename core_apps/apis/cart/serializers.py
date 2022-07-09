import logging
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from core_apps.core.cart.models import Cart
from core_apps.core.menu.models import FoodGallery

logger = logging.getLogger(__name__)


class CartSerializer(serializers.ModelSerializer):
    food_image = serializers.SerializerMethodField(read_only=True)
    food_price = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    updated_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cart
        fields = (
            "id",
            "user",
            "food",
            "food_price",
            "quantity",
            "sub_total",
            "food_image",
            "created_at",
            "updated_at",
        )

    def get_food_image(self, obj):
        if FoodGallery.objects.filter(food=obj.food).exists():
            food_gallery = FoodGallery.objects.get(food=obj.food)
            return food_gallery.food_images.url
        return None

    def get_food_price(self, obj):
        return str(obj.food.price) + " dh"

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
        if instance.user.username:
            data["user"] = instance.user.username

        if instance.food.food_name:
            data["food"] = instance.food.food_name

        return data

    def validate(self, attrs):
        quantity = attrs.get("quantity", None)
        if not quantity:
            raise serializers.ValidationError(
                {"quantity": _("This field is required.")}
            )

        return attrs

    def create(self, validated_data):
        if Cart.objects.filter(
            user=validated_data["user"], food=validated_data["food"]
        ).exists():
            cart = Cart.objects.get(
                user=validated_data["user"],
                food=validated_data["food"],
            )
            cart.quantity += validated_data["quantity"]
            cart.save()
            return cart

        return Cart.objects.create(**validated_data)
