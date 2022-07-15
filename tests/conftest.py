import pytest

from django.conf import settings
from django.db.models.signals import (
    pre_save,
    post_save,
    pre_delete,
    post_delete,
    m2m_changed,
)

from tests.core.menu.factories import FoodFactory, CategoryFactory
from tests.core.orders.factories import OrderFactory, OrderItemFactory
from tests.core.payments.factories import PaymentFactory
from tests.core.users.factories import UserFactory

from rest_framework.test import APIClient


@pytest.fixture
def user() -> settings.AUTH_USER_MODEL:
    return UserFactory()


@pytest.fixture
def superuser() -> settings.AUTH_USER_MODEL:
    return UserFactory(superuser=True)


@pytest.fixture
def food():
    category = CategoryFactory()
    food = FoodFactory(category=category)
    return food


@pytest.fixture
def order(user):
    payment = PaymentFactory(user=user)
    order = OrderFactory(user=user, payment=payment)
    return order


@pytest.fixture
def orderitem(order, food):
    orderitem = OrderItemFactory(
        order=order, user=order.user, payment=order.payment, food=food
    )
    return orderitem


@pytest.fixture
def api_client():
    return APIClient()


class CustomRequest(object):
    def __init__(self, user=None):
        self.user = user


# https://www.cameronmaske.com/muting-django-signals-with-a-pytest-fixture/
@pytest.fixture(autouse=True)  # Automatically use in tests.
def mute_signals(request):
    # Skip applying, if marked with `enabled_signals`
    if "enable_signals" in request.keywords:
        return

    signals = [pre_save, post_save, pre_delete, post_delete, m2m_changed]
    restore = {}
    for signal in signals:
        # Temporally remove the signal's receivers (a.k.a attached functions)
        restore[signal] = signal.receivers
        signal.receivers = []

    def restore_signals():
        # When the test tears down, restore the signals.
        for signal, receivers in restore.items():
            signal.receivers = receivers

    # Called after a test has finished.
    request.addfinalizer(restore_signals)
