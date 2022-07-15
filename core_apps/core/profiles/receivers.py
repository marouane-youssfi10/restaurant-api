from django.db.models.signals import post_save
from django.dispatch import receiver

from celery import current_app

from core_apps.core.users.models import User


@receiver(post_save, sender=User, dispatch_uid="create_customer_profile")
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        current_app.send_task(
            "core_apps.core.profiles.tasks.create_customer_profile", args=[instance.id]
        )
