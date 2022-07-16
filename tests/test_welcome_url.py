import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_welcome(api_client):
    response = api_client.get(reverse("welcome"))
    assert response.status_code == status.HTTP_200_OK, response.content
