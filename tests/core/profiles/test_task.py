from unittest.mock import patch

import pytest

from core_apps.core.profiles.tasks import create_customer_profile

from tests.core.users.factories import UserFactory


@pytest.mark.django_db
@pytest.mark.skip(reason="'enable_signals' not found in `markers` configuration option")
@patch("core_apps.core.profiles.tasks.create_customer_profile")
def test_create_customer_profile(mock_create_customer_profile):
    user = UserFactory()
    create_customer_profile.apply(user.pkid)
    mock_create_customer_profile.assert_called_once_with(user.pkid)
    assert mock_create_customer_profile.call_count == 1
