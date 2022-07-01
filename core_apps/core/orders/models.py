from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from core_apps.core.common.models import TimeStampedUUIDModel
from core_apps.core.orders.managers import (
    OrderManager,
    AcceptedOrderManager,
    CompletedOrderManager,
    CancledOrderManager,
)

User = get_user_model()


class Order(TimeStampedUUIDModel):
    class Gender(models.TextChoices):
        NEW = "new", _("new")
        ACCEPTED = "accepted", _("accepted")
        COMPLETED = "completed,", _("completed,")
        CANCLED = "cancled", _("cancled")

    user = models.ForeignKey(
        User,
        verbose_name=_("user"),
        related_name="user_order",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    payment = models.ForeignKey(
        "payments.Payment",
        verbose_name=_("payment"),
        related_name="payment_order",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    order_number = models.CharField(
        verbose_name=_("order number"), max_length=50, blank=True, null=True
    )
    address = models.CharField(
        verbose_name=_("address"), max_length=100, blank=False, null=False
    )
    country = CountryField(
        verbose_name=_("country"), max_length=100, blank=False, null=False
    )
    city = models.CharField(
        verbose_name=_("city"), max_length=100, blank=False, null=False
    )
    order_note = models.CharField(
        verbose_name=_("order note"), max_length=100, blank=True, null=True
    )
    order_total = models.FloatField(
        verbose_name=_("order total"), max_length=100, blank=True, null=True
    )
    status = models.CharField(
        verbose_name=_("status"),
        max_length=10,
        choices=Gender.choices,
        default=Gender.NEW,
    )
    is_ordered = models.BooleanField(verbose_name=_("is ordered"), default=False)

    objects = OrderManager()

    def __str__(self):
        return str(self.order_number)


class AcceptedOrder(Order):

    objects = AcceptedOrderManager()

    class Meta:
        verbose_name = "Order accepted"
        verbose_name_plural = "Orders accepted"
        proxy = True


class CompletedOrder(Order):

    objects = CompletedOrderManager()

    class Meta:
        verbose_name = "Order completed"
        verbose_name_plural = "Orders completed"
        proxy = True


class CancledOrder(Order):

    objects = CancledOrderManager()

    class Meta:
        verbose_name = "Order cancled"
        verbose_name_plural = "Orders cancled"
        proxy = True


class OrderItem(TimeStampedUUIDModel):
    user = models.ForeignKey(
        User,
        related_name="user_orderitems",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    payment = models.ForeignKey(
        "payments.Payment",
        verbose_name=_("payment"),
        related_name="payment_orderitem",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    order = models.ForeignKey(
        Order,
        verbose_name=_("order"),
        related_name=_("order_orderitems"),
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    food = models.ForeignKey(
        "menu.Food",
        on_delete=models.CASCADE,
        related_name=_("food_orderitems"),
        verbose_name=_("food"),
        blank=False,
        null=False,
    )
    quantity = models.IntegerField(verbose_name=_("quantity"), default=1)
    food_price = models.FloatField(
        verbose_name=_("food price"), blank=False, null=False
    )
    ordered = models.BooleanField(verbose_name=_("ordered"), default=False)

    def __str__(self):
        return f"{self.user.username} - {self.order}"
