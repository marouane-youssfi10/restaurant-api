import pytest
from django.urls import reverse
from rest_framework import status

from tests.core.profiles.factories import CustomerFactory


@pytest.mark.django_db
def test_category_retrieve(api_client, user):
    customer = CustomerFactory(user=user)
    url = reverse(
        "customers:profiles-detail",
        args=[
            customer.pkid,
        ],
    )
    assert url == f"/api/profiles/{customer.pkid}/"
    api_client.force_authenticate(user)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK, response.content
    print(response.json())
    assert response.json()["customer"]["full_name"] == customer.user.get_full_name
    assert response.json()["customer"]["gender"] == customer.gender
    assert response.json()["customer"]["city"] == customer.city
    assert response.json()["customer"]["photo_profile"] == str("/mediafiles/") + str(
        customer.user.profile_photo
    )
    assert response.json()["customer"]["email"] == customer.user.email
