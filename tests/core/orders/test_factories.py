import pytest

from tests.core.orders.factories import OrderFactory, OrderItemFactory


@pytest.mark.django_db
def test_order_factory():
    order = OrderFactory()
    assert order.pkid


@pytest.mark.django_db
def test_order_item_factory():
    orderitem = OrderItemFactory()
    assert orderitem.pkid
