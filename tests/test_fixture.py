import pytest


@pytest.mark.django_db
def test_order(order):
    assert order.id
    assert order.user
    assert order.payment


@pytest.mark.django_db
def test_orderitem(orderitem, order):
    assert orderitem.id
    assert orderitem.user
    assert orderitem.payment
    assert orderitem.order
    assert orderitem.food
    assert orderitem.order == order
    assert orderitem.user == order.user
    assert orderitem.payment == order.payment
