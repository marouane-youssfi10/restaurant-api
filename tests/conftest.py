import pytest

from django.conf import settings

from tests.core.users.factories import UserFactory


@pytest.fixture
def user() -> settings.AUTH_USER_MODEL:
    return UserFactory()


@pytest.fixture
def superuser() -> settings.AUTH_USER_MODEL:
    return UserFactory(superuser=True)


class CustomRequest(object):
    def __init__(self, user=None):
        self.user = user
