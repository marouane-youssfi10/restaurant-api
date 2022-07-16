import pytest

from core_apps.apis.payments.exceptions import OrderNumberDoesNotExist


@pytest.mark.django_db
def test_payments_exceptions(user):
    order_nuber_does_not_exist = OrderNumberDoesNotExist()
    assert order_nuber_does_not_exist.status_code == 404
    assert order_nuber_does_not_exist.detail == "This Order Does Not exists"
