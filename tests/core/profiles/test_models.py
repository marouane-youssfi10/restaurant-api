import pytest

from tests.core.profiles.factories import CustomerFactory


@pytest.mark.django_db
def test_customer__str__(user):
    customer = CustomerFactory()
    assert customer.__str__() == f"{customer.user.username}"


@pytest.mark.django_db
def test_customer__phone_numbers_and_country():
    instance = CustomerFactory(phone_number="+21299005099", country="Morocco")
    assert instance.id
    assert instance.phone_number
    assert instance.country
