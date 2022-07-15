from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from core_apps.core.common.models import TimeStampedUUIDModel
from core_apps.core.profiles.managers import CustomerManager

User = get_user_model()


class Customer(TimeStampedUUIDModel):
    class Gender(models.TextChoices):
        MALE = "male", _("male")
        FEMALE = "female", _("female")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(
        verbose_name=_("gender"),
        choices=Gender.choices,
        max_length=20,
        null=True,
        blank=True,
    )
    phone_number = PhoneNumberField(verbose_name=_("phone number"), max_length=30)
    address = models.CharField(
        verbose_name=_("address"), max_length=100, null=True, blank=True
    )
    country = CountryField(
        verbose_name=_("country"), max_length=100, blank=False, null=False
    )
    city = models.CharField(
        verbose_name=_("city"), max_length=100, blank=False, null=False
    )

    objects = CustomerManager()

    def __str__(self):
        return f"{self.user.username}"
