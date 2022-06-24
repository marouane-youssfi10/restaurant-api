import pytest

from tests.core.profiles.factories import CustomerFactory


@pytest.mark.django_db
def test_profiles_factories():
    instance = CustomerFactory()
    assert instance.id
