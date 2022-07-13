import pytest


@pytest.mark.django_db
def test_order__str__(user, order):
    assert order.__str__() == f"{order.user.username}'s " + str(order.order_number)
