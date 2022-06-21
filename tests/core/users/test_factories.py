import pytest

from tests.core.users.factories import UserFactory


@pytest.mark.django_db
def test_user_factory():
    user = UserFactory()
    assert user.id
    assert not user.is_staff and not user.is_superuser
    super_user = UserFactory(superuser=True)
    assert super_user.id
    assert super_user.is_staff
    assert super_user.is_superuser
