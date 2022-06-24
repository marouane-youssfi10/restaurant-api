from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommonConfig(AppConfig):
    name = "core_apps.core.common"
    verbose_name = _("Common")
