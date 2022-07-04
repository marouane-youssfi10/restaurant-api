from unittest.mock import patch

import pytest

from tests.core.orders.factories import OrderItemFactory

from tests.core.payments.factories import PaymentFactory
from core_apps.core.payments.tasks import update_order_payment, create_orderitem


@pytest.mark.django_db
@pytest.mark.skip(reason="'enable_signals' not found in `markers` configuration option")
@patch("core_apps.core.payments.tasks.update_order_payment")
def test_update_order_payment(mock_update_order_payment, user):
    payment = PaymentFactory(user=user)
    update_order_payment.apply(payment.pkid)
    assert mock_update_order_payment.call_count == 1
    mock_update_order_payment.assert_called_once_with(payment.pkid)


@pytest.mark.django_db
@pytest.mark.skip(reason="'enable_signals' not found in `markers` configuration option")
@patch("core_apps.core.payments.tasks.create_orderitem")
def test_create_orderitem(mock_create_orderitem, orderitem):
    orderitem = OrderItemFactory()
    create_orderitem.apply(orderitem.pkid)
    assert mock_create_orderitem.call_count == 1
    mock_create_orderitem.assert_called_once_with(orderitem.pkid)
