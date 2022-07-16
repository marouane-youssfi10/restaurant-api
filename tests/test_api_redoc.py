import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_api_redoc(client):
    response = client.get(reverse("schema-redoc"), {"format": "openapi"})
    assert response.status_code == status.HTTP_200_OK, response.content
