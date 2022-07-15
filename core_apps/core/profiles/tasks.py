import logging

from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist

from core_apps.core.orders.models import User
from core_apps.core.profiles.models import Customer

logger = logging.getLogger(__name__)


@shared_task(
    name="core_apps.core.profiles.tasks.create_customer_profile",
    autoretry_for=(ObjectDoesNotExist,),
    default_retry_delay=5,
    max_retries=5,
)
def create_customer_profile(pk):
    user = User.objects.get(id=pk)
    Customer.objects.create(user=user)
