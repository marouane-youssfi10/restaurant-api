from django.contrib import admin

from core_apps.core.payments.models import Payment
from core_apps.utils.admin import ReadOnlyWithDetailAdmin


class PaymentAdmin(ReadOnlyWithDetailAdmin):
    list_display = [
        "pkid",
        "user",
        "method",
        "amount_paid",
        "status",
        "created_at",
    ]
    list_display_links = ["pkid", "user"]
    list_filter = ["method", "status"]


admin.site.register(Payment, PaymentAdmin)
