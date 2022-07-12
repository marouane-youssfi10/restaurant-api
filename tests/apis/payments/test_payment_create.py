import pytest
from django.urls import reverse
from rest_framework import status

from core_apps.core.orders.models import Order
from core_apps.core.payments.models import Payment
from tests.core.orders.factories import OrderFactory


@pytest.mark.django_db
def test_payment_create(api_client, user):
    order = OrderFactory(user=user, is_ordered=False)
    url = reverse("payments:payment-list")
    assert url == "/api/payments/payment/"
    assert Order.objects.all().count() == 1
    assert Payment.objects.all().count() == 1
    api_client.force_authenticate(user)
    response = api_client.post(
        url,
        data={
            "user": order.user.pkid,
            "method": "paypal",
            "amount_paid": order.order_total,
            "status": "successful",
        },
    )
    assert response.status_code == status.HTTP_201_CREATED, response.content
    assert Payment.objects.all().count() == 2
    assert response.json()["user"] == order.user.pkid
    assert response.json()["method"] == "paypal"
    assert float(response.json()["amount_paid"]) == order.order_total
    assert response.json()["status"] == "successful"


@pytest.mark.django_db
def test_payment_create_with_no_order(api_client, user):
    url = reverse("payments:payment-list")
    assert url == "/api/payments/payment/"
    api_client.force_authenticate(user)
    response = api_client.post(
        url,
        data={
            "user": user.pkid,
            "method": "paypal",
            "amount_paid": 42.50,
            "status": "successful",
        },
    )
    no_order = ["There's no Order for this user '" + str(user) + "'"]
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content
    assert response.json()["non_field_errors"] == no_order
