import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.core.payments.managers import PaymentManager

User = get_user_model()


class Payment(models.Model):
    class PaymentMethods(models.TextChoices):
        paypal = "paypal", _("paypal")
        stripe = "stripe", _("stripe")

    class Status(models.TextChoices):
        SUCCESSFUL = "successful", _("successful")
        FAILED = "failed", _("failed")

    payment_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_payment"
    )
    method = models.CharField(
        verbose_name=_("Method payment"),
        choices=PaymentMethods.choices,
        max_length=20,
        null=False,
        blank=False,
    )
    amount_paid = models.CharField(max_length=100)
    status = models.CharField(
        verbose_name=_("Method payment"),
        choices=Status.choices,
        max_length=20,
        null=False,
        blank=False,
    )

    objects = PaymentManager()

    def __str__(self):
        return f"{self.method}"
