import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_order_by_status_listing(api_client, user, order):
    api_client.force_authenticate(user)
    url = reverse("orders:order-list")
    assert url == f"/api/orders/order/"
    response = api_client.get(url + str("?status=" + order.status))
    assert response.status_code == status.HTTP_200_OK, response.content
    assert response.json()[0]["user"] == order.user.pkid
    assert response.json()[0]["payment"] == order.payment.pkid
    assert response.json()[0]["order_number"] == order.order_number
    assert response.json()[0]["status"] == order.status
    # check if there's no status in path like ?status=
    response = api_client.get(url + str("?"))
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content
    assert response.json()["detail"] == "you must pass status in params"
