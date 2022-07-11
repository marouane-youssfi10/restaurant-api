import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_order_status_patch(api_client, user, order):
    url = reverse(
        "orders:order-detail",
        args=[
            order.pkid,
        ],
    )
    assert url == f"/api/orders/order/{order.pkid}/"
    api_client.force_authenticate(user)
    response = api_client.patch(url, data={"status": "accepted"})
    assert response.status_code == status.HTTP_200_OK, response.content
    # check the Order does not exist
    url1 = reverse(
        "orders:order-detail",
        args=[
            0,
        ],
    )
    assert url1 == f"/api/orders/order/0/"
    response = api_client.patch(url1, data={"status": "accepted"})
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.content
    assert response.json()["detail"] == "Order Does Not Exist"
