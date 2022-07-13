import pytest
from rest_framework import status

from core_apps.core.orders.models import Order
from tests.core.orders.factories import OrderFactory


@pytest.mark.django_db
def test_order_admin_with_status_accepted__create(superuser, client):
    client.force_login(superuser)
    order = OrderFactory(with_status_accepted=True)
    response = client.post(
        "/admin/orders/acceptedorder/add/",
        {
            "user": order.user,
            "order_number": order.order_number,
            "payment": order.payment,
            "address": order.address,
            "country": order.country,
            "city": order.city,
            "order_total": order.order_total,
        },
        follow=True,
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    response = client.get(f"/admin/orders/acceptedorder/{order.pkid}/change/")
    assert str(order.user.username), str(order.status) in str(response.content)
    assert str(order.status) in Order.Statues.ACCEPTED


@pytest.mark.django_db
def test_order_admin_with_status_completed__create(superuser, client):
    client.force_login(superuser)
    order = OrderFactory(with_status_completed=True)
    response = client.post(
        "/admin/orders/completedorder/add/",
        {
            "user": order.user,
            "order_number": order.order_number,
            "payment": order.payment,
            "address": order.address,
            "country": order.country,
            "city": order.city,
            "order_total": order.order_total,
        },
        follow=True,
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    response = client.get(f"/admin/orders/completedorder/{order.pkid}/change/")
    assert str(order.user.username), str(order.status) in str(response.content)
    assert str(order.status) in str(response.content), Order.Statues.COMPLETED


@pytest.mark.django_db
def test_order_admin_with_status_cancled__create(superuser, client):
    client.force_login(superuser)
    order = OrderFactory(with_status_cancled=True)
    response = client.post(
        "/admin/orders/cancledorder/add/",
        {
            "user": order.user,
            "order_number": order.order_number,
            "payment": order.payment,
            "address": order.address,
            "country": order.country,
            "city": order.city,
            "order_total": order.order_total,
        },
        follow=True,
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    response = client.get(f"/admin/orders/cancledorder/{order.pkid}/change/")
    assert str(order.user.username), str(order.status) in str(response.content)
    assert str(order.status) in str(response.content), Order.Statues.CANCLED


@pytest.mark.django_db
def test_update_order_payment_and_set_status_to_accepted(order):
    Order.objects.update_order_payment_and_set_status_to_accpeted(order, order.payment)
    assert order.status == Order.Statues.ACCEPTED


@pytest.mark.django_db
def test_set_order_status_to_cancled(order):
    Order.objects.set_order_status_to_cancled(order)
    assert order.status == Order.Statues.CANCLED
