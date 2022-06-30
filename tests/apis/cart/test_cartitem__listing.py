import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_cartitem_listing(api_client, user):
    api_client.force_authenticate(user)
    url = reverse("carts:cartitems-list")
    assert url == "/api/carts/cartitems/"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK, response.content
