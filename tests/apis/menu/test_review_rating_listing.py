import pytest
from django.urls import reverse
from rest_framework import status

from tests.core.menu.factories import ReviewRatingFactory


@pytest.mark.django_db
def test_review_rating_listing(api_client, user, food):
    review_rating = ReviewRatingFactory(user=user, food=food)
    api_client.force_authenticate(user)
    url = reverse(
        "menu:review-rating-list",
    )
    assert url == "/api/menu/review-rating/"
    response = api_client.get(url + str("?by_food=" + review_rating.food.slug))
    assert response.status_code == status.HTTP_200_OK, response.content
    assert "results" in response.json()
    assert response.json()["count"] == 1
    assert response.json()["results"][0]["food"] == str(review_rating.food)
    assert response.json()["results"][0]["review"] == review_rating.review
    assert response.json()["results"][0]["rating"] == review_rating.rating
