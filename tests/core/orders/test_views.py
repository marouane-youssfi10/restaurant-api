import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_order_autocomplete(api_client, order):
    url = reverse("order-autocomplete")
    response = api_client.get(url + "?q=" + str(order.order_number))
    assert response.status_code == status.HTTP_200_OK
