import pytest

from tests.core.orders.factories import OrderFactory, OrderItemFactory


@pytest.mark.django_db
def test_order_factory():
    instance = OrderFactory()
    assert instance.id
    assert instance.user


@pytest.mark.django_db
def test_order_item_factory():
    instance = OrderItemFactory()
    assert instance.id
    assert instance.user
    assert instance.order
    assert instance.food
