import logging

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from core_apps.apis.menu.exceptions import (
    ReviewUserDoesNotExists,
    AlreadyRated,
    FoodDoesNotExist,
)
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
        category_image = None
        if obj.category_image:
            return obj.category_image.url
        return category_image

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


class ReviewRatingSerializer(serializers.ModelSerializer):
    food = serializers.StringRelatedField(read_only=False)
    created_at = serializers.SerializerMethodField(read_only=True)
    updated_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ReviewRating
        fields = (
            "id",
            "food",
            "review",
            "rating",
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
        data["profile_photo"] = None
        data["username"] = instance.user.username
        if instance.user.profile_photo:
            data["profile_photo"] = instance.user.profile_photo.url
        return data

    def validate(self, attrs):
        if "review" in attrs and "rating" in attrs and "food" in self.initial_data:
            food = self.initial_data["food"]
            # check if food pkid is exists
            if not Food.objects.filter(pkid=food).exists():
                raise FoodDoesNotExist

            # check if the user Already Rated on post food
            if (
                ReviewRating.objects.filter(
                    user=self.context["request"].user, food=food
                ).count()
                >= 1
            ):
                raise AlreadyRated
            return attrs

        # check this review user if exists
        user = self.context["request"].user
        try:
            ReviewRating.objects.get(user__username=user)
        except ReviewRating.DoesNotExist:
            logger.error(f"the review of this user {user} does not exists")
            raise ReviewUserDoesNotExists

        return attrs

    def create(self, validated_data):
        food = self.initial_data.get("food", None)
        review_rating = ReviewRating.objects.create(
            user=self.context["request"].user,
            food_id=food,
            review=validated_data["review"],
            rating=validated_data["rating"],
        )
        review_rating.save()

        return review_rating

    def update(self, instance, validated_data):
        review_rating = ReviewRating.objects.get(user__username=instance)
        review_rating.review = validated_data["review"]
        review_rating.save()

        return review_rating
