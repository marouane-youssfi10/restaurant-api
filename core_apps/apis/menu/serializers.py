import logging

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from core_apps.core.menu.models import Category, Food, FoodGallery, ReviewRating

logger = logging.getLogger(__name__)


class CategorySerializer(serializers.ModelSerializer):
    category_image = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField(read_only=True)
    updated_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "category_name",
            "slug",
            "description",
            "category_image",
            "created_at",
            "updated_at",
        )

    def get_category_image(self, obj):
        if obj.category_image:
            return obj.category_image.url
        return ""

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


class FoodSerializer(serializers.ModelSerializer):
    food_image = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    updated_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Food
        fields = (
            "id",
            "food_name",
            "slug",
            "description",
            "price",
            "food_image",
            "created_at",
            "updated_at",
        )

    def get_food_image(self, obj):
        food_image = None
        try:
            food = Food.objects.get(id=obj.id)
            food_gallery = FoodGallery.objects.get(food=food)
            if food_gallery.food_images:
                food_image = food_gallery.food_images.url
        except ObjectDoesNotExist:
            pass

        return food_image

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


class FoodGallerySerializer(serializers.ModelSerializer):
    food_images = serializers.SerializerMethodField(read_only=True)
    food_info = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    updated_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = FoodGallery
        fields = (
            "id",
            "food_images",
            "created_at",
            "updated_at",
            "food_info",
        )

    def get_food_info(self, obj):
        return {
            "id": obj.food.id,
            "food_name": obj.food.food_name,
            "price": obj.food.price,
        }

    def get_food_images(self, obj):
        if obj.food_images:
            return obj.food_images.url
        return ""

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


class ReviewRatingSerializer(serializers.ModelSerializer):
    food_info = serializers.SerializerMethodField(read_only=True)
    user_info = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    updated_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ReviewRating
        fields = (
            "id",
            "review",
            "rating",
            "created_at",
            "updated_at",
            "user_info",
            "food_info",
        )

    def get_food_info(self, obj):
        return {
            "id": obj.food.id,
            "food_name": obj.food.food_name,
            "price": obj.food.price,
        }

    def get_user_info(self, obj):
        if obj.user.profile_photo:
            profile_photo = obj.user.profile_photo.url
        else:
            profile_photo = ""
        return {
            "id": obj.user.id,
            "username": obj.user.username,
            "profile_photo": profile_photo,
        }

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
