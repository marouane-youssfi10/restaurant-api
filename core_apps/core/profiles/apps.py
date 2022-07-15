from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProfilesConfig(AppConfig):
    name = "core_apps.core.profiles"
    verbose_name = _("Profiles")

    def ready(self):
        import core_apps.core.profiles.receivers  # noqa F401
