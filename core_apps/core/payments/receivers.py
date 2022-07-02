from celery import current_app
from django.db.models.signals import post_save
from django.dispatch import receiver

from core_apps.core.payments.models import Payment


@receiver(
    post_save, sender=Payment, dispatch_uid="update_order_payment_and_create_orderitem"
)
def update_order_payment_and_create_orderitem(instance, created, **kwargs):
    if created:
        current_app.send_task(
            "core_apps.core.payments.tasks.update_order_payment_and_create_orderitem",
            args=[instance.pkid],
        )
