from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from core_apps.core.cart.managers import CartManager
from core_apps.core.common.models import TimeStampedUUIDModel
from core_apps.core.menu.models import Food

User = get_user_model()


class Cart(TimeStampedUUIDModel):
    user = models.ForeignKey(
        User, verbose_name=_("user"), related_name="cart", on_delete=models.CASCADE
    )

    food = models.ForeignKey(
        Food, verbose_name=_("food"), related_name="foods", on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, default=1)

    objects = CartManager()

    def __str__(self):
        return f"{self.user.username}'s - cart"

    def sub_total(self):
        return self.food.price * self.quantity
