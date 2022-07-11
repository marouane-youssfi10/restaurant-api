import pytest
from django.urls import reverse
from rest_framework import status

from core_apps.core.cart.models import Cart
from core_apps.core.orders.models import Order
from tests.core.cart.factories import CartFactory


@pytest.mark.django_db
def test_order_create(api_client, user, food):
    # create Cart for avoid raising error "there's no foods in carts"
    CartFactory(user=user, food=food, quantity=1)
    url = reverse("orders:order-list")
    assert url == "/api/orders/order/"
    api_client.force_authenticate(user)
    response = api_client.post(
        url,
        data={
            "user": user.pkid,
            "order_number": "300620221",
            "address": "street 1",
            "country": "Morocco",
            "city": "meknes",
            "order_total": 25.0,
        },
    )
    order = Order.objects.get(user=user)
    assert response.status_code == status.HTTP_201_CREATED, response.content
    assert Cart.objects.all().count() == 1
    assert response.json()["user"] == order.user.pkid
    assert response.json()["order_number"] == order.order_number
    assert response.json()["country"] == "Morocco"
    assert response.json()["city"] == order.city
    assert response.json()["order_total"] == order.order_total
    # check if there's more than one orders
    response = api_client.post(
        url,
        data={
            "user": user.pkid,
            "order_number": "300620221",
            "address": "street 1",
            "country": "Morocco",
            "city": "meknes",
            "order_total": 25.0,
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content
    assert response.json()["detail"] == "you have already order not completed"


@pytest.mark.django_db
def test_order_create_with_cart_empty(api_client, user):
    url = reverse("orders:order-list")
    assert url == "/api/orders/order/"
    api_client.force_authenticate(user)
    response = api_client.post(
        url,
        data={
            "user": user.pkid,
            "order_number": "300620221",
            "address": "street 2",
            "country": "Italy",
            "city": "Roma",
            "order_total": 25.0,
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content
    assert (
        response.json()["detail"] == "You must have one food in your cartitem at least"
    )
