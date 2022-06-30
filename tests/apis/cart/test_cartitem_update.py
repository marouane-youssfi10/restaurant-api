import pytest
from django.urls import reverse
from rest_framework import status

from tests.core.cart.factories import CartFactory


@pytest.mark.django_db
def test_address_update(api_client, user, food):
    cart = CartFactory(user=user, food=food)
    url = reverse(
        "carts:cartitems-detail",
        args=[
            cart.pkid,
        ],
    )
    assert url == f"/api/carts/cartitems/{cart.pkid}/"
    api_client.force_authenticate(user)
    response = api_client.patch(url, data={"quantity": 2})
    assert response.status_code == status.HTTP_200_OK, response.content
    assert response.json()["quantity"] == 2
    cart.refresh_from_db()
    assert cart.quantity == 2
