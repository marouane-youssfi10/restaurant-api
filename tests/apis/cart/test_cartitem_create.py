import pytest
from django.urls import reverse
from rest_framework import status

from core_apps.core.cart.models import Cart


@pytest.mark.django_db
def test_cart_create(api_client, user, food):
    url = reverse("carts:cartitems-list")
    assert url == "/api/carts/cartitems/"
    api_client.force_authenticate(user)
    response1 = api_client.post(
        url,
        data={"user": user.pkid, "food": food.pkid, "quantity": 2},
    )
    assert response1.status_code == status.HTTP_201_CREATED, response1.content
    assert response1.json()["user"] == str(user)
    assert response1.json()["food"] == str(food)
    assert response1.json()["quantity"] == 2
    assert Cart.objects.all().count() == 1
    response2 = api_client.post(
        url,
        data={"user": user.pkid, "food": food.pkid, "quantity": 1},
    )
    assert response2.status_code == status.HTTP_201_CREATED, response2.content
    # check if the new cart is increased not created new one separate
    assert Cart.objects.all().count() == 1

    # check the quantity field is required
    response3 = api_client.post(
        url,
        data={"user": user.pkid, "food": food.pkid},
    )
    assert response3.status_code == status.HTTP_400_BAD_REQUEST, response3.content
    assert response3.json()["quantity"] == ["This field is required."]
