import pytest

from core_apps.apis.orders.exceptions import (
    CartItemIsEmpty,
    HaveMoreOrders,
    NoStatusInParams,
)


@pytest.mark.django_db
def test_orders_exceptions(user):
    cart_item_is_empty = CartItemIsEmpty()
    assert cart_item_is_empty.status_code == 400
    assert (
        cart_item_is_empty.detail == "You must have one food in your cartitem at least"
    )

    have_more_orders = HaveMoreOrders()
    assert have_more_orders.status_code == 400
    assert have_more_orders.detail == "you have already order not completed"

    no_status_in_params = NoStatusInParams()
    assert no_status_in_params.status_code == 400
    assert no_status_in_params.detail == "you must pass status in params"
