import pytest
from django.urls import reverse
from rest_framework import status

from core_apps.core.menu.models import FoodGallery
from tests.core.menu.factories import FoodGalleryFactory


@pytest.mark.django_db
def test_listing_food_by_name(api_client, user, food):
    food_image = FoodGalleryFactory.create(with_image=True, food=food)
    api_client.force_authenticate(user)
    url = reverse(
        "menu:foods-list",
    )
    assert url == f"/api/menu/foods/"
    response1 = api_client.get(url + str("?food_name=" + food_image.food.food_name))
    assert response1.status_code == status.HTTP_200_OK, response1.content
    assert "results" in response1.json()
    assert response1.json()["count"] == 1
    assert response1.json()["results"][0]["food_name"] == food_image.food.food_name
    assert response1.json()["results"][0]["slug"] == food_image.food.slug
    assert response1.json()["results"][0]["price"] == food_image.food.price
    assert response1.json()["results"][0]["food_image"] == str("/mediafiles/") + str(
        food_image.food_images
    )
    # check the image is none
    FoodGallery.objects.all().delete()
    FoodGalleryFactory.create(with_image=False)
    api_client.force_authenticate(user)
    url = reverse(
        "menu:foods-list",
    )
    assert url == f"/api/menu/foods/"
    response2 = api_client.get(url + str("?food_name="))
    assert response2.status_code == status.HTTP_200_OK, response2.content
    assert response2.json()["results"][0]["food_image"] is None


@pytest.mark.django_db
def test_listing_food_by_category(api_client, user, food):
    api_client.force_authenticate(user)
    url = reverse(
        "menu:foods-list",
    )
    assert url == f"/api/menu/foods/"
    response = api_client.get(url + str("?category_slug=" + food.category.slug))
    assert "results" in response.json()
    assert response.json()["count"] == 1
    assert response.json()["results"][0]["slug"] == food.slug
