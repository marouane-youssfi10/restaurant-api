import pytest
from django.contrib.admin import AdminSite
from rest_framework import status

from core_apps.core.orders.admin import OrderAdmin, OrderItemAdmin
from core_apps.core.orders.models import Order, OrderItem
from tests.conftest import CustomRequest
from tests.core.orders.factories import OrderFactory, OrderItemFactory
from tests.core.users.factories import UserFactory


@pytest.mark.django_db
def test_order_admin__save_model(client):
    user = UserFactory(superuser=True)
    order = OrderFactory(user=user)
    order_admin = OrderAdmin(model=Order, admin_site=AdminSite())
    order_admin.save_model(obj=order, request=None, form=None, change=None)
    assert order_admin.has_add_permission(CustomRequest(user)) == False
    assert order_admin.has_change_permission(CustomRequest(user)) == False
    assert order_admin.has_delete_permission(CustomRequest(user)) == False


@pytest.mark.django_db
def test_order_items_admin__save_model(client):
    user = UserFactory(superuser=True)
    orderitem = OrderItemFactory(user=user)
    order_item_admin = OrderItemAdmin(model=OrderItem, admin_site=AdminSite())
    order_item_admin.save_model(obj=orderitem, request=None, form=None, change=None)
    assert order_item_admin.has_add_permission(CustomRequest(user)) == False
    assert order_item_admin.has_change_permission(CustomRequest(user)) == False
    assert order_item_admin.has_delete_permission(CustomRequest(user)) == False


@pytest.mark.django_db
def test_order_admin__create(superuser, client, order):
    client.force_login(superuser)
    response = client.post(
        "/admin/orders/order/add/",
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
    response = client.get("/admin/orders/order/")
    # assert if any method in str(response.content) like (column-....)
    assert str(order.user.username) in str(response.content)


@pytest.mark.django_db
def test_order_admin__change(superuser, client, order):
    client.force_login(superuser)
    response = client.post(
        f"/admin/orders/order/{order.pkid}/change/",
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


@pytest.mark.django_db
def test_order_admin__delete(superuser, client, order):
    client.force_login(superuser)
    response = client.post(
        f"/admin/orders/order/{order.pkid}/delete/",
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_order_items_admin__create(superuser, client, orderitem):
    client.force_login(superuser)
    response = client.post(
        "/admin/orders/orderitem/add/",
        {
            "user": orderitem.user,
            "order": orderitem.order,
            "food": orderitem.food,
            "payment": orderitem.payment,
            "quantity": orderitem.quantity,
            "food_price": orderitem.food_price,
            "ordered": True,
        },
        follow=True,
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    response = client.get("/admin/orders/orderitem/")
    assert str(orderitem.user.username) in str(response.content)


@pytest.mark.django_db
def test_order_item_admin__change(superuser, client, orderitem):
    client.force_login(superuser)

    response = client.post(
        f"/admin/orders/orderitem/{orderitem.pkid}/change/",
        {
            "user": orderitem.user,
            "order": orderitem.order,
            "food": orderitem.food,
            "payment": orderitem.payment,
            "quantity": orderitem.quantity,
            "food_price": orderitem.food_price,
            "ordered": False,
        },
        follow=True,
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_order_item_admin__delete(superuser, client, orderitem):
    client.force_login(superuser)
    response = client.post(
        f"/admin/orders/orderitem/{orderitem.pkid}/delete/",
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
