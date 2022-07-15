import pytest
from django.urls import reverse
from rest_framework import status

from tests.core.profiles.factories import CustomerFactory


@pytest.mark.django_db
def test_customer_update(api_client, user, food):
    customer1 = CustomerFactory(user=user, phone_number="21264126212")
    url = reverse(
        "customers:profiles-detail",
        args=[
            customer1.pkid,
        ],
    )
    assert url == f"/api/profiles/{customer1.pkid}/"
    api_client.force_authenticate(user)
    # check partial_update customer profile
    customer2 = CustomerFactory()
    response = api_client.patch(
        url,
        data={
            "city": customer2.city,
        },
    )
    assert response.status_code == status.HTTP_200_OK, response.content
    assert response.json()["customer"]["city"] == customer2.city
    # check update customer profile
    customer3 = CustomerFactory(phone_number="+41524204242", country="Morocco")
    response = api_client.put(
        url,
        data={
            "gender": customer3.gender,
            "phone_number": customer3.phone_number,
            "address": customer3.address,
            "country": customer3.country,
            "city": customer3.city,
        },
    )
    assert response.status_code == status.HTTP_200_OK, response.content
    assert response.json()["customer"]["gender"] == customer3.gender
    assert response.json()["customer"]["phone_number"] == customer3.phone_number
    assert response.json()["customer"]["address"] == customer3.address
    assert response.json()["customer"]["country"] == customer3.country
    assert response.json()["customer"]["city"] == customer3.city
