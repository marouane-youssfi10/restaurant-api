from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import re_path as url

from core_apps.core.users.views import UserAutocompleteView

admin.autodiscover()

urlpatterns = [
    url(
        r"^user-autocomplete/$",
        UserAutocompleteView.as_view(),
        name="user-autocomplete",
    ),
    path(settings.ADMIN_URL, admin.site.urls),
]
