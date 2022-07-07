import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_category_listing(api_client, user):
    api_client.force_authenticate(user)
    url = reverse("menu:categories-list")
    assert url == "/api/menu/categories/"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK, response.content
