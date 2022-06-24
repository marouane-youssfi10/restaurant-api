from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OrdersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.core.orders"
    verbose_name = _("Orders")
