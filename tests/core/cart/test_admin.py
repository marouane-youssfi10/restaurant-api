import pytest
from django.contrib.admin import AdminSite
from rest_framework import status

from core_apps.core.cart.admin import CartAdmin
from core_apps.core.cart.models import Cart
from tests.conftest import CustomRequest
from tests.core.users.factories import UserFactory
from tests.core.menu.factories import FoodFactory
from tests.core.cart.factories import CartFactory


@pytest.mark.django_db
def test_cart_admin__save_model(client):
    user = UserFactory(superuser=True)
    cart = CartFactory.create(user=user)
    cart_admin = CartAdmin(model=Cart, admin_site=AdminSite())
    cart_admin.save_model(obj=cart, request=None, form=None, change=None)
    assert cart_admin.has_add_permission(CustomRequest(user)) == True
    assert cart_admin.has_change_permission(CustomRequest(user)) == True
    assert cart_admin.has_delete_permission(CustomRequest(user)) == True


@pytest.mark.django_db
def test_cart_admin__create(superuser, client):
    client.force_login(superuser)
    cart = CartFactory()
    response = client.post(
        "/admin/cart/cart/add/",
        {
            "user": cart.user,
            "food": cart.food,
            "quantity": cart.quantity,
        },
        follow=True,
    )
    assert response.status_code == status.HTTP_200_OK
    response = client.get("/admin/cart/cart/")
    assert str(cart.user.username) in str(response.content)


@pytest.mark.django_db
def test_cart_admin__change(superuser, client):
    client.force_login(superuser)
    user = UserFactory()
    food = FoodFactory()
    cart = CartFactory(user=user, food=food)
    response = client.post(
        f"/admin/cart/cart/{cart.pkid}/change/",
        {"user": cart.user, "food": cart.food, "quantity": cart.quantity},
        follow=True,
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_cart_admin__delete(superuser, client):
    client.force_login(superuser)
    user = UserFactory()
    food = FoodFactory()
    cart = CartFactory(user=user, food=food)
    response = client.post(f"/admin/cart/cart/{cart.pkid}/delete/")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_cart__sub_total(superuser, user, client, food):
    client.force_login(superuser)
    CartFactory.create(user=user, food=food, quantity=1)
    cart = Cart.objects.first()
    cart_admin = CartAdmin(model=Cart, admin_site=AdminSite())
    cart_admin.save_model(obj=cart, request=None, form=None, change=None)
    response = client.get("/admin/cart/cart/")
    assert "column-sub_total" in str(response.content)
