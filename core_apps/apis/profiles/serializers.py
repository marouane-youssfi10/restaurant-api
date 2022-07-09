import logging

from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from core_apps.core.profiles.models import Customer

logger = logging.getLogger(__name__)


class CustomersSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)
    country = CountryField(name_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    updated_at = serializers.SerializerMethodField(read_only=True)

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

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
        data["photo_profile"] = None
        if instance.user.profile_photo:
            data["photo_profile"] = instance.user.profile_photo.url
        data["email"] = instance.user.email

        return data

    class Meta:
        model = Customer
        fields = (
            "id",
            "full_name",
            "gender",
            "phone_number",
            "address",
            "country",
            "city",
            "created_at",
            "updated_at",
        )
