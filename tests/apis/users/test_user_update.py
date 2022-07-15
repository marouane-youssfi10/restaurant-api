import factory
import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_user_update(api_client, user):
    api_client.force_authenticate(user)
    url = reverse(
        "user:user-detail",
        args=[
            "me",
        ],
    )
    email = factory.Faker._get_faker().email()
    # first_name = factory.Faker._get_faker().first_name()
    # last_name = factory.Faker._get_faker().last_name()
    response = api_client.patch(
        url,
        data={
            "email": email,
            "username": "test test",
        },
    )
    assert url == "/api/users/me/"
    assert response.status_code == status.HTTP_200_OK, response.content
    assert response.json()["email"] == email
    assert response.json()["username"] == "test test"
