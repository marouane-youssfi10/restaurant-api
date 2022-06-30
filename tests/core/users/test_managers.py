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


@pytest.mark.django_db
def test_super_user_is_not_superuser(user):
    with pytest.raises(ValueError) as err:
        User.objects.create_superuser(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            username=user.username,
            password=user.password,
            is_superuser=False,
        )
    assert str(err.value) == "Superusers must have is_superuser=True"


@pytest.mark.django_db
def test_create_super_user_with_is_staff_equal_false(user):
    with pytest.raises(ValueError) as err:
        User.objects.create_superuser(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            username=user.username,
            password=user.password,
            is_superuser=True,
            is_staff=False,
        )
    assert str(err.value) == "Superusers must have is_staff=True"


@pytest.mark.django_db
def test_create_user_with_no_email(user):
    with pytest.raises(ValueError) as err:
        User.objects.create_user(
            first_name=user.first_name,
            last_name=user.last_name,
            email=None,
            username=user.username,
            password=user.password,
            is_superuser=False,
        )
    assert str(err.value) == "Base User Account: An email address is required"


@pytest.mark.django_db
def test_create_user_with_no_username(user):
    with pytest.raises(ValueError) as err:
        User.objects.create_user(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            username=None,
            password=user.password,
            is_superuser=False,
        )
    assert str(err.value) == "Users must submit a username"


@pytest.mark.django_db
def test_create_user_with_no_firstname(user):
    with pytest.raises(ValueError) as err:
        User.objects.create_user(
            first_name=None,
            last_name=user.last_name,
            email=user.email,
            username=user.email,
            password=user.password,
            is_superuser=False,
        )
    assert str(err.value) == "Users must submit a first name"


@pytest.mark.django_db
def test_create_user_with_no_lastname(user):
    with pytest.raises(ValueError) as err:
        User.objects.create_user(
            first_name=user.first_name,
            last_name=None,
            email=user.email,
            username=user.email,
            password=user.password,
            is_superuser=False,
        )
    assert str(err.value) == "Users must submit a last name"


@pytest.mark.django_db
def test_create_superuser_with_no_email(user):
    with pytest.raises(ValueError) as err:
        User.objects.create_superuser(
            first_name=user.first_name,
            last_name=user.first_name,
            email=None,
            username=user.email,
            password="test",
            is_superuser=True,
            is_staff=True,
        )
    assert str(err.value) == "Admin Account: An email address is required"


@pytest.mark.django_db
def test_create_superuser_with_no_password(user):
    with pytest.raises(ValueError) as err:
        User.objects.create_superuser(
            first_name=user.first_name,
            last_name=user.first_name,
            email=user.email,
            username=user.email,
            password=None,
            is_superuser=True,
            is_staff=True,
        )
    assert str(err.value) == "Superusers must have a password"


@pytest.mark.django_db
def test_user_email_incorrect(user):
    with pytest.raises(ValueError) as err:
        User.objects.email_validator(email="marouane.com")
    assert str(err.value) == "You must provide a valid email address"
