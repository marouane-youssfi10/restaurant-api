import pytest


@pytest.mark.django_db
@pytest.mark.skip(reason="Create CartFactory")
def test_cart__sub_total(superuser, client, food):
    pass
    # client.force_login(superuser)
    # user = UserFactory(superuser=True)
    # CartFactory.create(user=user, food=food, quantity=1)
    # cart = Cart.objects.first()
    # cart_admin = CartAdmin(model=Cart, admin_site=AdminSite())
    # cart_admin.save_model(obj=cart, request=None, form=None, change=None)
    # response = client.get("/admin/cart/cart/")
    # assert "column-sub_total" in str(response.content)
