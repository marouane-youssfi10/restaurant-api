import pytest
from django.urls import reverse
from rest_framework import status

from core_apps.core.cart.models import Cart


@pytest.mark.django_db
def test_cart_create(api_client, user, food):
    url = reverse("carts:cartitems-list")
    assert url == "/api/carts/cartitems/"
    api_client.force_authenticate(user)
    response = api_client.post(
        url,
        data={"user": user.pkid, "food": food.pkid, "quantity": 2},
    )
    assert response.status_code == status.HTTP_201_CREATED, response.content
    assert response.json()["user"] == str(user)
    assert response.json()["food"] == str(food)
    assert response.json()["quantity"] == 2
    assert Cart.objects.all().count() == 1
