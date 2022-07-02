import logging

from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist

from core_apps.core.cart.models import Cart
from core_apps.core.orders.models import Order, OrderItem
from core_apps.core.payments.models import Payment

logger = logging.getLogger(__name__)


@shared_task(
    name="core_apps.core.payments.tasks.update_order_payment",
    autoretry_for=(ObjectDoesNotExist,),
    default_retry_delay=5,
    max_retries=5,
)
def update_order_payment(pkid):
    payment = Payment.objects.get(pkid=pkid)
    order = Order.objects.filter(
        user=payment.user, status=Order.Gender.NEW, is_ordered=False
    ).latest("created_at")
    order.payment = payment
    order.is_ordered = True
    order.status = Order.Gender.ACCEPTED
    order.save()


@shared_task(
    name="core_apps.core.payments.tasks.create_orderitem",
    autoretry_for=(ObjectDoesNotExist,),
    default_retry_delay=5,
    max_retries=5,
)
def create_orderitem(pkid):
    payment = Payment.objects.get(pkid=pkid)
    cart_items = Cart.objects.filter(user=payment.user)
    order = Order.objects.filter(
        user=payment.user, status=Order.Gender.ACCEPTED, is_ordered=True
    ).latest("created_at")
    for item in cart_items:
        order_item = OrderItem.objects.create(
            user=order.user,
            payment=payment,
            order=order,
            food=item.food,
            quantity=item.quantity,
            food_price=item.food.price,
            ordered=True,
        )
        order_item.save()

    # Clear cart
    Cart.objects.filter(user=payment.user).delete()
