import pytest


@pytest.mark.django_db
@pytest.mark.skip(reason="Create CartFactory")
def test_cart__total_price(user, food):
    pass
    # cart = CartFactory(user=user, food=food, quantity=3)
    # assert cart.quantity == 3
    # sub_total1 = cart.food.price * cart.quantity
    # assert cart.sub_total == sub_total1
