import pytest

from tests.core.orders.factories import OrderFactory, OrderItemFactory


@pytest.mark.django_db
def test_order_factory():
    order = OrderFactory()
    assert order.id
    assert order.user
    assert order.payment


@pytest.mark.django_db
def test_order_item_factory():
    orderitem = OrderItemFactory()
    assert orderitem.id
    assert orderitem.user
    assert orderitem.order
    assert orderitem.payment
    assert orderitem.food
