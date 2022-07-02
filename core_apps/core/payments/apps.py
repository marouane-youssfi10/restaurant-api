from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PaymentsConfig(AppConfig):
    name = "core_apps.core.payments"
    verbose_name = _("Payments")

    def ready(self):
        import core_apps.core.payments.receivers  # noqa F401
