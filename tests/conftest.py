import pytest

from django.conf import settings

from tests.core.users.factories import UserFactory

from rest_framework.test import APIClient


@pytest.fixture
def user() -> settings.AUTH_USER_MODEL:
    return UserFactory()


@pytest.fixture
def superuser() -> settings.AUTH_USER_MODEL:
    return UserFactory(superuser=True)


@pytest.fixture
def api_client():
    return APIClient()


class CustomRequest(object):
    def __init__(self, user=None):
        self.user = user
