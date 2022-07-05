import pytest

from .factories import CartFactory


@pytest.mark.django_db
def test_cart_factory():
    instance = CartFactory()
    assert instance.pkid
