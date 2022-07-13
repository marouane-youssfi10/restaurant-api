import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_review_rating_create(api_client, user, food):
    # check if the user created successfully
    url = reverse("menu:review-rating-list")
    assert url == "/api/menu/review-rating/"
    api_client.force_authenticate(user)
    response1 = api_client.post(
        url,
        data={"food": food.pkid, "review": "good", "rating": 4.5},
    )
    assert response1.status_code == status.HTTP_201_CREATED, response1.content
    # check if the user already rated on food post
    print("\nresponse1.json()['food']", response1.json()["food"], "\n")
    print("\nfood.pkid", food.pkid, "\n")
    response2 = api_client.post(
        url,
        data={
            "food": food.pkid,
            "review": response1.json()["review"],
            "rating": response1.json()["rating"],
        },
    )
    assert response2.status_code == status.HTTP_400_BAD_REQUEST, response2.content
    assert response2.json()["detail"] == "You have already Rated this food"
    # check if this food pkid exists
    url = reverse("menu:review-rating-list")
    assert url == "/api/menu/review-rating/"
    api_client.force_authenticate(user)
    response = api_client.post(
        url,
        data={"food": food.pkid + 1, "review": "good", "rating": 4.5},
    )
    assert response.json()["detail"] == "Food Does Not Exist"
