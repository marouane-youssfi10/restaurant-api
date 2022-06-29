import pytest

from .factories import CartFactory

@pytest.mark.django_db
def test_cart_factory():
    instance = CartFactory()
    assert instance.id
    assert instance.user
    assert instance.food
