import factory
import pytest

from core_apps.core.users.models import User
from tests.core.users.factories import UserFactory


@pytest.mark.django_db
def test_user_manager__create():
    instance = UserFactory()
    assert instance.first_name
    assert instance.last_name
    assert instance.username
    assert instance.date_joined


@pytest.mark.django_db
def test_user_manager__normalize_email():
    instance = User.objects.normalize_email("Test@Gmail.com")
    # normalizes to domain to small letters
    assert instance == "Test@gmail.com"


@pytest.mark.django_db
def test_user_manager__create_user():
    first_name = factory.Faker._get_faker().first_name()
    last_name = factory.Faker._get_faker().last_name()
    username = first_name + last_name
    instance = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=factory.Faker._get_faker().email(),
        password=factory.Faker._get_faker().password(),
    )
    assert instance.id
    assert instance.username
    assert instance.password


@pytest.mark.django_db
def test_user_manager__create_superuser():
    first_name = factory.Faker._get_faker().first_name()
    last_name = factory.Faker._get_faker().last_name()
    username = first_name + last_name
    instance = User.objects.create_superuser(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=factory.Faker._get_faker().email(),
        password=factory.Faker._get_faker().password(),
    )
    assert instance.id
    assert instance.username
    assert instance.is_superuser
    assert instance.password
