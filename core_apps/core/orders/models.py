from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from core_apps.core.common.models import TimeStampedUUIDModel

User = get_user_model()


class Order(TimeStampedUUIDModel):
    class Gender(models.TextChoices):
        NEW = "new", _("new")
        ACCEPTED = "accepted", _("accepted")
        COMPLETED = "completed,", _("completed,")
        CANCLED = "cancled", _("cancled")

    user = models.ForeignKey(
        User, verbose_name=_("user"), related_name="order", on_delete=models.CASCADE
    )
    # payment = models.ForeignKey(
    #     "payment.Payment",
    #     verbose_name=_("payment"),
    #     related_name="payment_order",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True
    # )
    order_number = models.CharField(
        verbose_name=_("order number"), max_length=20, blank=False, null=False
    )
    address = models.CharField(
        verbose_name=_("address"), max_length=50, blank=False, null=False
    )
    country = CountryField(
        verbose_name=_("country"), max_length=50, blank=False, null=False
    )
    city = models.CharField(
        verbose_name=_("city"), max_length=50, blank=False, null=False
    )
    order_note = models.CharField(
        verbose_name=_("order note"), max_length=100, blank=True, null=True
    )
    order_total = models.FloatField(verbose_name=_("order total"))
    status = models.CharField(
        verbose_name=_("order total"),
        max_length=10,
        choices=Gender.choices,
        default="New",
    )
    is_ordered = models.BooleanField(verbose_name=_("is order"), default=False)

    def __str__(self):
        return self.order_number


class OrderItem(TimeStampedUUIDModel):
    user = models.ForeignKey(User, related_name="order_item", on_delete=models.CASCADE)
    # payment = models.ForeignKey(
    #     "payment.Payment",
    #     verbose_name=_("payment"),
    #     related_name="payment_order_item",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True
    # )
    order = models.ForeignKey(Order, verbose_name=_("order"), on_delete=models.CASCADE)
    # food = models.ForeignKey(
    #   "menu.Food", verbose_name=_("food"), blank=True, null=True
    # )
    quantity = models.IntegerField(verbose_name=_("quantity"))
    food_price = models.FloatField(verbose_name=_("food price"))
    ordered = models.BooleanField(verbose_name=_("ordered"), default=False)

    def __str__(self):
        return f"{self.user.username} - {self.order}"
