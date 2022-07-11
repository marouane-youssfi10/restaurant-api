import pytest
from django.urls import reverse
from rest_framework import status

from core_apps.core.orders.models import Order


@pytest.mark.django_db
def test_order_delete(api_client, user, order):
    url = reverse(
        "orders:order-detail",
        args=[
            order.pkid,
        ],
    )
    assert url == f"/api/orders/order/{order.pkid}/"
    api_client.force_authenticate(user)
    assert Order.objects.all().count() == 1
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.content
    assert Order.objects.all().count() == 0
