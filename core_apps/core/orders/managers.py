import typing
from django.db import models

if typing.TYPE_CHECKING:
    from core_apps.core.orders.models import Order


class OrderQuerySet(models.QuerySet):
    pass


class OrderManager(models.Manager):
    def create(self, *args: typing.Any, **kwargs: typing.Any) -> "Order":
        return super().create(*args, **kwargs)

    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)

    def all_new_orders(self):
        return self.get_queryset().filter(status="new")

    def update_order_payment_and_set_status_to_accpeted(self, order, payment):
        order.payment = payment
        order.is_ordered = True
        order.status = Order.Gender.ACCEPTED
        order.save()

    def set_order_status_to_cancled(self, order):
        order.status = Order.Gender.CANCLED
        order.save()


class AcceptedOrderManager(OrderManager):
    def all_order_accepted(self):
        return self.get_queryset().filter(status="accepted")


class CompletedOrderManager(OrderManager):
    def all_order_completed(self):
        return self.get_queryset().filter(status="completed")


class CancledOrderManager(OrderManager):
    def all_order_cancled(self):
        return self.get_queryset().filter(status="cancled")


class OrderItemManager(models.Manager):
    pass
