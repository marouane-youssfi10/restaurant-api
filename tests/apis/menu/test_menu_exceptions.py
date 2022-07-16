import pytest

from core_apps.apis.menu.exceptions import (
    ReviewUserDoesNotExists,
    AlreadyRated,
    OrderDoesNotExist,
    FoodDoesNotExist,
)


@pytest.mark.django_db
def test_menu_exceptions(user):
    review_user_does_exists = ReviewUserDoesNotExists()
    assert review_user_does_exists.status_code == 400
    assert review_user_does_exists.detail == "the review of this user does not exist"

    already_rated = AlreadyRated()
    assert already_rated.status_code == 400
    assert already_rated.detail == "You have already Rated this food"

    order_does_not_exist = OrderDoesNotExist()
    assert order_does_not_exist.status_code == 404
    assert order_does_not_exist.detail == "Order Does Not Exist"

    food_does_not_exist = FoodDoesNotExist()
    assert food_does_not_exist.status_code == 404
    assert food_does_not_exist.detail == "Food Does Not Exist"
