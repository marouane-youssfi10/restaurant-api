import pytest
from django.contrib.admin import AdminSite
from rest_framework import status

from core_apps.core.orders.admin import OrderAdmin, OrderItemAdmin
from core_apps.core.orders.models import Order, OrderItem
from tests.conftest import CustomRequest
from tests.core.menu.factories import FoodFactory
from tests.core.orders.factories import OrderFactory, OrderItemFactory
from tests.core.users.factories import UserFactory


@pytest.mark.django_db
def test_order_admin__save_model(client):
    user = UserFactory(staff=True)
    order = OrderFactory.create(user=user)
    order_admin = OrderAdmin(model=Order, admin_site=AdminSite())
    order_admin.save_model(obj=order, request=None, form=None, change=None)
    assert order_admin.has_add_permission(order) == False
    assert order_admin.has_change_permission(order) == False
    assert order_admin.has_delete_permission(order) == False


@pytest.mark.django_db
def test_order_items_admin__save_model(client):
    user = UserFactory(superuser=True)
    order = OrderFactory(user=user)
    food = FoodFactory()
    order_item = OrderItemFactory.create(user=user, order=order, food=food)
    order_item_admin = OrderItemAdmin(model=OrderItem, admin_site=AdminSite())
    order_item_admin.save_model(obj=order_item, request=None, form=None, change=None)
    assert order_item_admin.has_add_permission(CustomRequest(user)) == True
    assert order_item_admin.has_change_permission(CustomRequest(user)) == True
    assert order_item_admin.has_delete_permission(CustomRequest(user)) == True


@pytest.mark.django_db
def test_order_admin__create(superuser, client):
    client.force_login(superuser)
    order = OrderFactory()
    response = client.post(
        "/admin/orders/order/add/",
        {
            "user": order.user,
            "order_number": order.order_number,
            "address": order.address,
            "country": order.country,
            "city": order.city,
            "order_total": order.order_total,
        },
        follow=True,
    )
    assert response.status_code == status.HTTP_200_OK
    response = client.get("/admin/orders/order/")
    # assert if any method in str(response.content) like (column-....)
    assert str(order.user.username) in str(response.content)


@pytest.mark.django_db
def test_order_admin__change(superuser, client):
    client.force_login(superuser)
    order = OrderFactory()
    response = client.post(
        f"/admin/orders/order/{order.pkid}/change/",
        {
            "user": order.user,
            "order_number": order.order_number,
            "address": order.address,
            "country": order.country,
            "city": order.city,
            "order_total": order.order_total,
        },
        follow=True,
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_order_admin__delete(superuser, client):
    client.force_login(superuser)
    order = OrderFactory()
    response = client.post(
        f"/admin/orders/order/{order.pkid}/delete/",
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_order_items_admin__create(superuser, client):
    client.force_login(superuser)
    user = UserFactory()
    order = OrderFactory(user=user)
    food = FoodFactory()
    order_item = OrderItemFactory(user=user, order=order, food=food)
    response = client.post(
        "/admin/orders/orderitem/add/",
        {
            "user": order_item.user,
            "order": order_item.order,
            "food": order_item.food,
            "quantity": order_item.quantity,
            "food_price": order_item.food_price,
            "ordered": False,
        },
        follow=True,
    )
    assert response.status_code == status.HTTP_200_OK
    response = client.get("/admin/orders/orderitem/")
    # assert if any method in str(response.content) like (column-....)
    assert str(order_item.user.username) in str(response.content)


@pytest.mark.django_db
def test_order_item_admin__change(superuser, client):
    client.force_login(superuser)
    user = UserFactory()
    order = OrderFactory(user=user)
    food = FoodFactory()
    order_item = OrderItemFactory(order=order, user=user, food=food)
    response = client.post(
        f"/admin/orders/orderitem/{order_item.pkid}/change/",
        {
            "user": order_item.user,
            "order": order_item.order,
            "food": order_item.food,
            "quantity": order_item.quantity,
            "food_price": order_item.food_price,
            "ordered": False,
        },
        follow=True,
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_order_item_admin__delete(superuser, client):
    client.force_login(superuser)
    user = UserFactory()
    order = OrderFactory(user=user)
    response = client.post(
        f"/admin/orders/order/{order.pkid}/delete/",
    )
    assert response.status_code == status.HTTP_200_OK
