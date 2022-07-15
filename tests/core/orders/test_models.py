import pytest


@pytest.mark.django_db
def test_order__str__(user, order):
    assert order.__str__() == str(order)


@pytest.mark.django_db
def test_order_item__str__(user, orderitem):
    assert orderitem.__str__() == str(orderitem.order)
