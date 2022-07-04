import pytest
from django.urls import reverse
from rest_framework import status

from tests.core.menu.factories import FoodGalleryFactory


@pytest.mark.django_db
def test_food_gallery_retrieve(api_client, user, food):
    food_gallery_image = FoodGalleryFactory(with_image=True, food=food)
    url = reverse(
        "menu:food-gallery-detail",
        args=[
            food_gallery_image.pkid,
        ],
    )
    assert url == f"/api/menu/food-gallery/{food_gallery_image.pkid}/"
    api_client.force_authenticate(user)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK, response.content
    assert response.json()["food_info"]["food_name"] == food.food_name
    assert response.json()["food_info"]["price"] == food.price
    assert response.json()["food_images"] == "/mediafiles/" + str(
        food_gallery_image.food_images
    )
    # get gallery image without image
    food_gallery_image = FoodGalleryFactory(with_image=False, food=food)
    url = reverse(
        "menu:food-gallery-detail",
        args=[
            food_gallery_image.pkid,
        ],
    )
    assert url == f"/api/menu/food-gallery/{food_gallery_image.pkid}/"
    api_client.force_authenticate(user)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK, response.content
    assert response.json()["food_images"] == ""
