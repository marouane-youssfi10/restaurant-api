import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_order_status_patch(api_client, user, order):
    url = reverse(
        "orders:order-detail",
        args=[
            order.pkid,
        ],
    )
    assert url == f"/api/orders/order/{order.pkid}/"
    api_client.force_authenticate(user)
    response = api_client.patch(url, data={"status": "accepted"})
    assert response.status_code == status.HTTP_200_OK, response.content
    # review_rating = ReviewRatingFactory.create(user=user)
    # url = reverse(
    #     "menu:review-rating-detail",
    #     args=[review_rating.pkid],
    # )
    # assert url == f"/api/menu/review-rating/{review_rating.pkid}/"
    # api_client.force_authenticate(user)
    # response = api_client.patch(url, data={"review": "review test updated"})
    # assert response.status_code == status.HTTP_200_OK, response.content
    # assert response.json()["review"] == "review test updated"
