import pytest
import factory

from django.contrib.admin import AdminSite
from rest_framework import status

from core_apps.core.users.admin import UserAdmin
from core_apps.core.users.models import User
from tests.conftest import CustomRequest
from tests.core.users.factories import UserFactory


@pytest.mark.django_db
def test_user_admin__create(superuser, client):
    client.force_login(superuser)
    password = factory.Faker._get_faker().password()
    email = factory.Faker._get_faker().email()
    response = client.post(
        "/admin/users/user/add/",
        {
            "email": email,
            "password1": password,
            "password2": password,
            "is_superuser": False,
            "is_staff": True,
            "is_active": True,
        },
        follow=True,
    )
    assert response.status_code == status.HTTP_200_OK
    assert User.objects.filter(email=email).exists()
    user = User.objects.get(email=email)
    assert not user.is_superuser
    assert user.is_staff
    assert user.is_active


@pytest.mark.django_db
def test_user_admin__save_model(client):
    user = UserFactory(superuser=True)
    user_admin = UserAdmin(model=User, admin_site=AdminSite())
    user_admin.save_model(obj=user, request=None, form=None, change=None)
    assert user_admin.has_add_permission(CustomRequest(user)) == True
    assert user_admin.has_change_permission(CustomRequest(user)) == True
    assert user_admin.has_delete_permission(CustomRequest(user)) == True
