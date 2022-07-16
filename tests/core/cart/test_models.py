import pytest

from tests.core.cart.factories import CartFactory


@pytest.mark.django_db
def test_cart__str__(user, food):
    cart = CartFactory(user=user, food=food, quantity=3)
    assert cart.__str__() == f"{cart.user.username}'s - cart"


@pytest.mark.django_db
def test_cart__total_price(user, food):
    cart = CartFactory(user=user, food=food, quantity=3)
    assert cart.quantity == 3
    assert cart.sub_total() == cart.food.price * cart.quantity
