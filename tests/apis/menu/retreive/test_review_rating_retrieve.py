import pytest
from django.urls import reverse
from rest_framework import status

from tests.core.menu.factories import ReviewRatingFactory


@pytest.mark.django_db
def test_review_rating_retrieve(api_client, user, food):
    review_rating = ReviewRatingFactory(user=user, food=food)
    url = reverse(
        "menu:review-rating-detail",
        args=[
            review_rating.pkid,
        ],
    )
    assert url == f"/api/menu/review-rating/{review_rating.pkid}/"
    api_client.force_authenticate(user)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK, response.content
    assert response.json()["review"] == review_rating.review
    assert response.json()["rating"] == review_rating.rating
    assert response.json()["user_info"]["email"] == review_rating.user.email
    assert response.json()["user_info"]["first_name"] == review_rating.user.first_name
    assert response.json()["user_info"]["last_name"] == review_rating.user.last_name
    assert response.json()["food_info"]["food_name"] == review_rating.food.food_name
    assert response.json()["food_info"]["price"] == review_rating.food.price
