from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OrdersConfig(AppConfig):
    name = "core_apps.core.orders"
    verbose_name = _("Orders")
