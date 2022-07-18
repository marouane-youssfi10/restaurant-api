import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_user_autocomplete(api_client, user):
    url = reverse("user-autocomplete")
    response = api_client.get(url + "?q=" + str(user.first_name))
    assert response.status_code == status.HTTP_200_OK
