import pytest

from tests.core.payments.factories import PaymentFactory


@pytest.mark.django_db
def test_payment_factory():
    instance = PaymentFactory()
    assert instance.id
    assert instance.user
