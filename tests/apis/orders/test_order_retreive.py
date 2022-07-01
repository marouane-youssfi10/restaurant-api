import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_order_retrieve(api_client, user, order):
    url = reverse(
        "orders:order-detail",
        args=[
            order.pkid,
        ],
    )
    assert url == f"/api/orders/order/{order.pkid}/"
    api_client.force_authenticate(user)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK, response.content
    assert response.json()["user"] == order.user.pkid
    assert response.json()["order_number"] == order.order_number
    assert response.json()["order_total"] == order.order_total
