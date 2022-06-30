import pytest
from django.urls import reverse
from rest_framework import status

from core_apps.core.cart.models import Cart
from tests.core.cart.factories import CartFactory


@pytest.mark.django_db
def test_address_delete(api_client, user):
    cart = CartFactory(user=user)
    url = reverse(
        "carts:cartitems-detail",
        args=[
            cart.pkid,
        ],
    )
    assert url == f"/api/carts/cartitems/{cart.pkid}/"
    api_client.force_authenticate(user)
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.content
    assert not Cart.objects.filter(id=cart.id).exists()
