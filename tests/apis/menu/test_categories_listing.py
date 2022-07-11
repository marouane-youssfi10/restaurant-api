import pytest
from django.urls import reverse
from rest_framework import status

from tests.core.menu.factories import CategoryFactory


@pytest.mark.django_db
def test_category_listing(api_client, user, food):
    api_client.force_authenticate(user)
    url = reverse(
        "menu:categories-list",
    )
    assert url == f"/api/menu/categories/"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK, response.content
    assert len(response.json()) == 1
    assert response.json()[0]["category_name"] == food.category.category_name
    assert response.json()[0]["category_image"] is None
    # create categories with images
    category = CategoryFactory(with_image=True)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK, response.content
    assert len(response.json()) == 2
    assert response.json()[1]["category_image"] == str("/mediafiles/") + str(
        category.category_image
    )
