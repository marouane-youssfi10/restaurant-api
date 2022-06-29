import logging

from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from core_apps.core.profiles.models import Customer

logger = logging.getLogger(__name__)


class CustomersSerializer(serializers.ModelSerializer):
    user_info = serializers.SerializerMethodField(read_only=True)
    full_name = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    updated_at = serializers.SerializerMethodField(read_only=True)
    country = CountryField(name_only=True)

    def get_user_info(self, obj):
        return {
            "pkid": obj.user.pkid,
            "username": obj.user.username,
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name,
            "email": obj.user.email,
            # "profile_photo": obj.user.profile_photo.url,
        }

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

    def get_created_at(self, obj):
        print("\nobj.created_at = ", obj.created_at, "\n")
        now = obj.created_at
        formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date

    def get_updated_at(self, obj):
        then = obj.updated_at
        formatted_date = then.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date

    class Meta:
        model = Customer
        fields = (
            "id",
            "user_info",
            "full_name",
            "gender",
            "phone_number",
            "address",
            "country",
            "city",
            "created_at",
            "updated_at",
        )
