import pytest
from django.contrib.admin import AdminSite
from rest_framework import status

from core_apps.core.payments.admin import PaymentAdmin
from core_apps.core.payments.models import Payment
from tests.conftest import CustomRequest
from tests.core.payments.factories import PaymentFactory
from tests.core.users.factories import UserFactory


@pytest.mark.django_db
def test_payment_admin__save_model(client):
    user = UserFactory(superuser=True)
    payment = PaymentFactory.create(user=user)
    payment_admin = PaymentAdmin(model=Payment, admin_site=AdminSite())
    payment_admin.save_model(obj=payment, request=None, form=None, change=None)
    assert payment_admin.has_add_permission(CustomRequest(user)) == False
    assert payment_admin.has_change_permission(CustomRequest(user)) == False
    assert payment_admin.has_delete_permission(CustomRequest(user)) == False


@pytest.mark.django_db
def test_payment_admin__create(superuser, client):
    client.force_login(superuser)
    payment = PaymentFactory()
    response = client.post(
        "/admin/payments/payment/add/",
        {
            "user": payment.user,
            "method": payment.method,
            "amount_paid": payment.amount_paid,
            "status": payment.status,
        },
        follow=True,
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    response = client.get("/admin/payments/payment/")
    assert str(payment.user.username) in str(response.content)


@pytest.mark.django_db
def test_payment_admin__change(superuser, client):
    client.force_login(superuser)
    payment = PaymentFactory()
    response = client.post(
        f"/admin/payments/payment/{payment.id}/change/",
        {
            "user": payment.user,
            "method": payment.method,
            "amount_paid": payment.amount_paid,
            "status": payment.status,
        },
        follow=True,
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_payment_admin__delete(superuser, client):
    client.force_login(superuser)
    payment = PaymentFactory()
    response = client.post(
        f"/admin/payments/payment/{payment.pkid}/delete/",
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
