import pytest
from django.urls import reverse
from rest_framework import status

from tests.core.menu.factories import CategoryFactory


@pytest.mark.django_db
def test_category_retrieve(api_client, user):
    category_with_image = CategoryFactory(with_image=True)
    url = reverse(
        "menu:categories-detail",
        args=[
            category_with_image.pkid,
        ],
    )
    assert url == f"/api/menu/categories/{category_with_image.pkid}/"
    api_client.force_authenticate(user)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK, response.content
    assert response.json()["category_name"] == category_with_image.category_name
    assert response.json()["category_image"] == "/mediafiles/" + str(
        category_with_image.category_image
    )
    category_without_image = CategoryFactory(with_image=False)
    url = reverse(
        "menu:categories-detail",
        args=[
            category_without_image.pkid,
        ],
    )
    response = api_client.get(url)
    assert url == f"/api/menu/categories/{category_without_image.pkid}/"
    assert response.status_code == status.HTTP_200_OK, response.content
    assert response.json()["category_image"] == ""
