import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_food_listing(api_client, user):
    api_client.force_authenticate(user)
    url = reverse("menu:food-gallery-list")
    assert url == "/api/menu/food-gallery/"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK, response.content
