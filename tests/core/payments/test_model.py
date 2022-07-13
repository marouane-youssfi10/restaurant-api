import pytest

from tests.core.payments.factories import PaymentFactory


@pytest.mark.django_db
def test_payments__str__(user):
    payment = PaymentFactory()
    assert payment.__str__() == f"{payment.method}"
