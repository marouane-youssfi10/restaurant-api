import pytest
from django.contrib.admin import AdminSite

from core_apps.core.profiles.admin import CustomerAdmin
from core_apps.core.profiles.models import Customer
from tests.conftest import CustomRequest
from tests.core.profiles.factories import CustomerFactory
from tests.core.users.factories import UserFactory


@pytest.mark.django_db
def test_customer_admin__save_model(client):
    user = UserFactory(superuser=True)
    customer = CustomerFactory.create(user=user)
    customer_admin = CustomerAdmin(model=Customer, admin_site=AdminSite())
    customer_admin.save_model(obj=customer, request=None, form=None, change=None)
    assert customer_admin.has_add_permission(CustomRequest(user)) == True
    assert customer_admin.has_change_permission(CustomRequest(user)) == True
    assert customer_admin.has_delete_permission(CustomRequest(user)) == True
