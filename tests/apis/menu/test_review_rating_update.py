import pytest
from django.urls import reverse
from rest_framework import status

from core_apps.core.menu.models import ReviewRating
from tests.core.menu.factories import ReviewRatingFactory


@pytest.mark.django_db
def test_review_rating_update(api_client, user):
    # check if the updating of review rating run successfully
    review_rating = ReviewRatingFactory.create(user=user)
    url = reverse(
        "menu:review-rating-detail",
        args=[review_rating.pkid],
    )
    assert url == f"/api/menu/review-rating/{review_rating.pkid}/"
    api_client.force_authenticate(user)
    response = api_client.patch(url, data={"review": "review test updated"})
    assert response.status_code == status.HTTP_200_OK, response.content
    assert response.json()["review"] == "review test updated"
    # check if this user exists
    ReviewRating.objects.all().delete()
    review_rating = ReviewRatingFactory.create()
    url = reverse(
        "menu:review-rating-detail",
        args=[review_rating.pkid],
    )
    assert url == f"/api/menu/review-rating/{review_rating.pkid}/"
    api_client.force_authenticate(user)
    response = api_client.patch(url, data={"review": "review test updated"})
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content
    assert response.json()["detail"] == "the review of this user does not exist"
