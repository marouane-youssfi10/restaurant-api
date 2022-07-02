import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_order_retrieve(api_client, user, order):
    url = reverse(
        "payments:payment-detail",
        args=[
            order.payment.pkid,
        ],
    )
    assert url == f"/api/payments/payment/{order.payment.pkid}/"
    api_client.force_authenticate(user)
    response = api_client.get(url)
    print("response.json() = ", response.json())
    assert response.status_code == status.HTTP_200_OK, response.content
    assert response.json()["user"] == order.payment.user.pkid
    assert int(response.json()["amount_paid"]) == order.payment.amount_paid
