import pytest
from django.urls import reverse
from rest_framework import status

from tests.core.menu.factories import CategoryFactory


@pytest.mark.django_db
def test_category_retrieve(api_client, user):
    category = CategoryFactory()
    url = reverse(
        "menu:categories-detail",
        args=[
            category.pkid,
        ],
    )
    assert url == f"/api/menu/categories/{category.pkid}/"
    api_client.force_authenticate(user)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK, response.content
    assert response.json()["category_name"] == category.category_name
