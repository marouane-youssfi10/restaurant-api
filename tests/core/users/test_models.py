import pytest


@pytest.mark.django_db
def test_user__str__(user):
    assert user.__str__() == f"{user.username}"


@pytest.mark.django_db
def test_user__get_full_name(user):
    assert user.get_full_name == f"{user.first_name} {user.last_name}"
